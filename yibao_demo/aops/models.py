import uuid
from django.db import models
from django.core.validators import MaxValueValidator


class EmployeeUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empno = models.BigIntegerField(unique=True, db_index=True, validators=[MaxValueValidator(50000)], verbose_name='编号')
    name = models.CharField(max_length=64, verbose_name='用户名')
    group = models.ManyToManyField('Organization', through='GroupMember', related_name='emp')

    def __str__(self):
        return self.name


class Organization(models.Model):
    TypeEnum = (
        ('dev', '开发',),
        ('test', '测试',),
        ('ops', '运维',),
        ('prod', '产品',),

    )
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='组织名称')
    type = models.CharField(max_length=5, choices=TypeEnum, default="dev", verbose_name='类型')

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    employee_user = models.ForeignKey(EmployeeUser, related_name='membership', on_delete=models.CASCADE)
    group = models.ForeignKey(Organization, related_name='membership', on_delete=models.CASCADE)

    def __str__(self):
        return "%s is in group %s" % (self.employee_user, self.group)
