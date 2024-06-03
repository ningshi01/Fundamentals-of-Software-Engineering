from django.db import models
from decimal import Decimal

from user.models import User, Passenger


class Station(models.Model):
    name = models.CharField(max_length=5, unique=True, verbose_name="车站名", null=False)
    city = models.CharField(max_length=10, verbose_name="城市名", null=False)

    class Meta:
        verbose_name = '车站'
        verbose_name_plural = '车站'
        ordering = ['-id']


class Train(models.Model):
    train_type_choices = (
        ('HSR', '高铁'),
        ('REG', '普通车'),
    )

    name = models.CharField(max_length=128, unique=True, verbose_name="车次", null=False)
    train_type = models.CharField(max_length=8, choices=train_type_choices, default="HSR", verbose_name="车次类型",
                                  null=False)

    class Meta:
        verbose_name = '列车'
        verbose_name_plural = '列车'
        ordering = ['-id']


class Stop(models.Model):
    train = models.ForeignKey(Train, verbose_name='车次', on_delete=models.CASCADE, null=False)
    station = models.ForeignKey(Station, verbose_name='车站', on_delete=models.CASCADE, null=False)
    arrival_time = models.TimeField(verbose_name='到达时间')
    duration = models.DurationField(verbose_name='停留时间')
    # 出发时间根据上面两项计算，以处理跨天的情况
    sequence = models.IntegerField(verbose_name='序号', null=False)

    class Meta:
        verbose_name = '途径站'
        verbose_name_plural = '途径站'
        ordering = ['-id']


class Carriage(models.Model):
    type_choices = (
        ('BUS', '商务舱'),
        ('FST', '一等舱'),
        ('SND', '二等舱'),
        ('SOF', '软卧'),
        ('HAW', '硬卧'),
        ('HAZ', '硬座'),
    )

    carriage_num = models.PositiveSmallIntegerField(verbose_name='车厢号')
    type = models.CharField(max_length=3, choices=type_choices, verbose_name='车厢类型')
    total_num = models.PositiveSmallIntegerField(verbose_name='座位总数')
    train = models.ForeignKey(Train, on_delete=models.CASCADE, verbose_name='所属车次')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'), verbose_name='价格')

    class Meta:
        verbose_name = '车厢'
        verbose_name_plural = '车厢'
        ordering = ['-id']


class Ticket(models.Model):
    date = models.DateField()
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    carriage = models.ForeignKey(Carriage, on_delete=models.CASCADE)
    remaining_count = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = '车票'
        verbose_name_plural = '车票'
        ordering = ['-id']


class Order(models.Model):
    order_status_choices = (
        ('PAD', '已支付'),
        ('UPD', '未支付'),
        ('EXP', '已过期'),  # Expired
    )

    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE, null=False)
    train = models.ForeignKey(Train, verbose_name='车次', on_delete=models.CASCADE, null=False)
    start_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='start_stop_order')
    end_stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='end_stop_order')
    create_time = models.DateTimeField(verbose_name='创建时间', null=False)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'), verbose_name='价格')
    order_status = models.CharField(max_length=3, verbose_name='订单状态')
    date = models.DateField()

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'
        ordering = ['-id']


class Seat(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    seat_num = models.PositiveSmallIntegerField()
    seat_location = models.CharField(max_length=1)
    is_available = models.BooleanField(default=True)


class PassengerOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'), verbose_name='价格')
    is_rebooked = models.BooleanField(default=False)
