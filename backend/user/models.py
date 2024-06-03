from django.db import models


class AbstractUser(models.Model):
    username = models.CharField(max_length=128, unique=True, verbose_name="用户名", null=False)
    password = models.CharField(max_length=256, verbose_name="密码", null=False)

    def __str__(self):
        return '<id=%s> %s' % (self.id, self.username)


class User(AbstractUser):
    email = models.EmailField(null=True, verbose_name="邮箱地址")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['-id']


class Passenger(models.Model):
    id_type_choices = (
        ('CIC', '中国居民身份证'),  # chinese_id_card
        ('HTP', '港澳居民来往内地通行证'),  # hkm_travel_permit
        ('TTP', '台湾居民来往大陆通行证'),  # taiwan_travel_permit
        ('PSP', '护照'),  # passport
        ('FRI', '外国人永久居留身份证'),  # foreign_resident_id
        ('HMT', '港澳台居民居住证'),  # hmt_residence_permit
    )

    ticket_type_choices = (
        ('ADU', '成人'),  # adult
        ('CHI', '儿童'),  # child
        ('STU', '学生'),  # student
        ('DOM', '残军'),  # disable or military
    )

    phone_region_choices = (
        ('86', '+86'),
        ('852', '+852'),
        ('853', '+853'),
        ('886', '+886'),
    )

    id_type = models.CharField(max_length=3, choices=id_type_choices, default='chinese_id_card',
                               verbose_name="证件类型", null=False)
    name = models.CharField(max_length=128, verbose_name="姓名", null=False)
    id_number = models.CharField(max_length=32, verbose_name="证件号码", null=False)
    ticket_type = models.CharField(max_length=3, choices=ticket_type_choices, default='adult',
                                   verbose_name="优惠(待)类型", null=False)
    phone_region = models.CharField(max_length=3, choices=phone_region_choices, default='86', verbose_name="地区",
                                    null=False)
    phone_number = models.CharField(max_length=32, verbose_name="手机号码", null=False)
    user = models.ForeignKey(User, verbose_name='关联用户', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '<id=%s> %s' % (self.id, self.name)

    class Meta:
        verbose_name = '乘车人'
        verbose_name_plural = '乘车人'
        ordering = ['-id']


class SystemAdmin(AbstractUser):
    class Meta:
        verbose_name = '系统管理员'
        verbose_name_plural = '系统管理员'
        ordering = ['-id']


class RailwayAdmin(AbstractUser):
    class Meta:
        verbose_name = '铁路系统员'
        verbose_name_plural = '铁路系统员'
        ordering = ['-id']
