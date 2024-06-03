import decimal
import logging

from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response

from user.models import User, Passenger, SystemAdmin, RailwayAdmin, AbstractUser
from user.token import generate_token, verify_token, get_identity_from_token

logger = logging.getLogger(__name__)


@api_view(['POST'])
def register(request):
    try:
        data = request.data
        username = data['username']

        same_name_user = User.objects.filter(username=username)
        if same_name_user:
            message = '用户名已存在'
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

        user = User()
        user.username = username
        user.password = make_password(data['password'])
        user.email = data['email']
        user.save()

        message = '用户注册成功'
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def get_user_info(request):
    try:
        user_token = request.META.get('HTTP_AUTHORIZATION', '')
        if verify_token(user_token):
            user_id = get_identity_from_token(user_token)
        else:
            message = f'token失效, token={user_token}'
            return Response({'message': message, 'token': user_token}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            message = '用户不存在'
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

        user_detail = {
            'username': user.username,
            'email': user.email,
            'balance': user.balance,
        }

        passengers = Passenger.objects.filter(user=user)

        passenger_list = []
        for passenger in passengers:
            passenger_info = {
                'id': passenger.id,
                'name': passenger.name,
                'id_type': passenger.id_type,
                'id_number': passenger.id_number,
                'ticket_type': passenger.ticket_type,
                'phone_region': passenger.phone_region,
                'phone_number': passenger.phone_number,
            }
            passenger_list.append(passenger_info)

        user_detail['passengers'] = passenger_list
        return Response(user_detail, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def get_admin_info(request):
    try:
        user_token = request.META.get('HTTP_AUTHORIZATION', '')
        if verify_token(user_token):
            user_id = get_identity_from_token(user_token)
        else:
            message = 'token失效'
            return Response({'message': message, 'token': user_token}, status=status.HTTP_401_UNAUTHORIZED)
        user = AbstractUser.objects.get(id=user_id)
        data = {
            'username': user.username,
        }
        message = '获取管理员信息成功'
        return Response({'message': message, 'data': data}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_user_info(request):
    try:
        user_token = request.META.get('HTTP_AUTHORIZATION', '')
        if verify_token(user_token):
            user_id = get_identity_from_token(user_token)
        else:
            message = 'token失效'
            return Response({'message': message, 'token': user_token}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        user = User.objects.get(id=user_id)

        if 'username' in data:
            username = data['username']
            if username != user.username:
                same_user = User.objects.filter(username=username).first()
                if same_user is not None:
                    message = '用户名已存在'
                    return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
            user.username = username

        # 检查是否要修改密码
        if 'password' in data:
            current_password = data['password'].get('current_password')
            new_password = data['password'].get('new_password')

            # 验证当前密码是否正确
            if not check_password(current_password, user.password):
                message = '原密码不正确'
                return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

            # 更新密码为新密码
            user.password = make_password(new_password)

        if 'email' in data:
            user.email = data['email']

        # 保存用户信息
        user.save()

        message = '用户信息更新成功'
        return Response({'message': message}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_passenger(request):
    try:
        data = request.data
        user_id = data['user_id']  # 可能是系统管理员调用次接口，需要传入响应用户id，而非当前用户id，所以不使用token
        user = User.objects.filter(id=user_id).first()

        if not user:
            message = '用户不存在'
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

        passenger = Passenger(
            id_type=data['id_type'],
            name=data['name'],
            id_number=data['id_number'],
            ticket_type=data['ticket_type'],
            phone_region=data['phone_region'],
            phone_number=data['phone_number'],
        )
        if Passenger.objects.filter(user_id=user_id, id_number=passenger.id_number):
            message = '该乘车人已存在'
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

        passenger.user = user
        passenger.save()
        message = '添加乘车人成功'
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def remove_passenger(request):
    try:
        data = request.data
        user_id = data['user_id']
        passenger_id = data['passenger_id']

        user = User.objects.get(id=user_id)
        passenger = Passenger.objects.get(id=passenger_id, user=user)
        passenger.delete()

        message = '删除乘车人成功'
        return Response({'message': message}, status=status.HTTP_200_OK)
    except (User.DoesNotExist, Passenger.DoesNotExist):
        message = '用户或乘车人不存在'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_passenger(request):
    try:
        data = request.data
        passenger_id = data['passenger_id']
        passenger = Passenger.objects.get(id=passenger_id)

        if 'ticket_type' in data:
            passenger.ticket_type = data['ticket_type']
        if 'phone_number' in data:
            passenger.phone_number = data['phone_number']

        passenger.save()

        message = '乘车人信息更新成功'
        return Response({'message': message}, status=status.HTTP_200_OK)
    except Passenger.DoesNotExist:
        message = '乘车人不存在'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def get_passenger_list(request):
    try:
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        passengers = user.passenger_set.all()

        passenger_list = []
        for passenger in passengers:
            passenger_list.append({
                'id': passenger.id,
                'name': passenger.name,
                'id_type': passenger.id_type,
                'id_number': passenger.id_number,
                'ticket_type': passenger.ticket_type,
                'phone_region': passenger.phone_region,
                'phone_number': passenger.phone_number,
            })
        message = '查询成功'
        return Response({'message': message, 'passenger_list': passenger_list}, status=status.HTTP_200_OK)

    except Exception as e:
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        user_type = ''
        try:
            # 依次尝试查询User、SystemAdmin和RailwayAdmin模型，查找匹配的用户
            user = User.objects.get(username=username)
            user_type = 'user'
        except User.DoesNotExist:
            try:
                user = SystemAdmin.objects.get(username=username)
                user_type = 'system_admin'
            except SystemAdmin.DoesNotExist:
                try:
                    user = RailwayAdmin.objects.get(username=username)
                    user_type = 'railway_admin'
                except RailwayAdmin.DoesNotExist:
                    message = '用户不存在'
                    return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

        if check_password(password, user.password):
            new_token = generate_token(user.id)
            data = {
                'user_id': user.id,
                'username': user.username,
                'token': new_token,
                'user_type': user_type,
            }
            message = '登录成功'
            return Response({'message': message, 'data': data}, status=status.HTTP_200_OK)
        else:
            message = '用户名或密码错误'
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def logout(request):
    try:
        user_token = request.META.get('HTTP_AUTHORIZATION', '')
        if verify_token(user_token):
            user_id = get_identity_from_token(user_token)
            user = User.objects.filter(id=user_id).first()
            message = f'{user_id}:{user.username}登出成功'
            logger.info(message)
            return Response({'message': message}, status=status.HTTP_200_OK)
        else:
            message = 'token无效'
            logger.info(message)
            return Response({'message': message, 'token': user_token}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def logoff(request):
    try:
        user_token = request.META.get('HTTP_AUTHORIZATION', '')
        if verify_token(user_token):
            user_id = get_identity_from_token(user_token)
        else:
            message = f'token失效, token={user_token}'
            return Response({'message': message, 'token': user_token}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = User.objects \
                .get(id=user_id)
        except User.DoesNotExist:
            message = '用户不存在'
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        # request.session.flush()
        message = '注销成功'
        return Response({'message': message}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def recharge(request):
    try:
        user_token = request.META.get('HTTP_AUTHORIZATION', '')
        if verify_token(user_token):
            user_id = get_identity_from_token(user_token)
        else:
            message = f'token失效, token={user_token}'
            return Response({'message': message, 'token': user_token}, status=status.HTTP_401_UNAUTHORIZED)
        amount = request.data.get('amount')
        user = User.objects.get(id=user_id)

        user.balance += decimal.Decimal(amount)
        user.save()

        message = '充值成功'
        return Response({'message': message}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_user_list(request):
    try:
        users = User.objects.all().values()
        system_admins = SystemAdmin.objects.all().values()
        railway_admins = RailwayAdmin.objects.all().values()

        user_data = list(users)
        system_admin_data = list(system_admins)
        railway_admin_data = list(railway_admins)

        message = '获取用户列表成功'
        response_data = {
            'message': message,
            'users': user_data,
            'system_admins': system_admin_data,
            'railway_admins': railway_admin_data
        }

        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def add_user(request):
    try:
        data = request.data
        user_type = data.get('user_type')

        if user_type == 'user':
            username = data.get('username')
            password = data.get('password')
            password = make_password(password)
            email = data.get('email')

            # 创建 User 模型对象
            user = User.objects.create(
                username=username,
                password=password,
                email=email
            )
            user.save()

        elif user_type == 'system_admin':
            username = data.get('username')
            password = data.get('password')
            password = make_password(password)

            # 创建 SystemAdmin 模型对象
            system_admin = SystemAdmin.objects.create(
                username=username,
                password=password
            )
            system_admin.save()

        elif user_type == 'railway_admin':
            username = data.get('username')
            password = data.get('password')
            password = make_password(password)

            # 创建 RailwayAdmin 模型对象
            railway_admin = RailwayAdmin.objects.create(
                username=username,
                password=password
            )
            railway_admin.save()

        else:
            message = '无效的用户类型'
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

        message = '添加用户成功'
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def update_user_info_system_admin(request):
    try:
        data = request.data
        user_id = data['user_id']
        user_type = data['user_type']

        if user_type == 'user':
            user = User.objects.get(id=user_id)
        elif user_type == 'system_admin':
            user = SystemAdmin.objects.get(id=user_id)
        elif user_type == 'railway_admin':
            user = RailwayAdmin.objects.get(id=user_id)
        else:
            message = '无效的用户类型'
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

        # 更新密码
        if 'password' in data:
            new_password = data['password']
            user.password = make_password(new_password)

        # 更新其他字段
        if 'username' in data:
            username = data['username']
            if username != user.username:
                same_user = AbstractUser.objects.filter(username=username).first()
                if same_user is not None:
                    message = '用户名已存在'
                    return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
            user.username = username
        if user_type == 'user' and 'email' in data:
            user.email = data['email']

        # 保存用户信息
        user.save()

        message = '用户信息更新成功'
        return Response({'message': message}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        message = '用户不存在'
        return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def remove_user(request):
    try:
        data = request.data
        user_id = data['user_id']
        user_type = data['user_type']

        if user_type == 'user':
            try:
                user = User.objects.get(id=user_id)
                user.delete()
                message = '删除用户成功'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                message = '用户不存在'
                return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

        elif user_type == 'system_admin':
            try:
                system_admin = SystemAdmin.objects.get(id=user_id)
                system_admin.delete()
                message = '删除系统管理员成功'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except SystemAdmin.DoesNotExist:
                message = '系统管理员不存在'
                return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

        elif user_type == 'railway_admin':
            try:
                railway_admin = RailwayAdmin.objects.get(id=user_id)
                railway_admin.delete()
                message = '删除铁路系统员成功'
                return Response({'message': message}, status=status.HTTP_200_OK)
            except RailwayAdmin.DoesNotExist:
                message = '铁路系统员不存在'
                return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

        else:
            message = '无效的用户类型'
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(str(e))
        message = '发生错误：{}'.format(str(e))
        return Response({'message': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
