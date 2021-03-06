# Generated by Django 3.0.3 on 2020-03-02 09:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.BigIntegerField(db_index=True, unique=True, validators=[django.core.validators.MaxValueValidator(50000)], verbose_name='编号')),
                ('name', models.CharField(max_length=64, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='组织名称')),
                ('type', models.CharField(choices=[('dev', '开发'), ('test', '测试'), ('ops', '运维'), ('prod', '产品')], default='dev', max_length=5, verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='aops.EmployeeUser')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='aops.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='employeeuser',
            name='group',
            field=models.ManyToManyField(related_name='emp', through='aops.GroupMember', to='aops.Organization'),
        ),
    ]
