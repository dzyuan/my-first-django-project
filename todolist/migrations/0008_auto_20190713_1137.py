# Generated by Django 2.2.1 on 2019-07-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20190711_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Innovation',
        ),
        migrations.RemoveField(
            model_name='project',
            name='budget',
        ),
        migrations.AddField(
            model_name='project',
            name='applybudget',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='申请资助'),
        ),
        migrations.AddField(
            model_name='project',
            name='innovation',
            field=models.TextField(default='', verbose_name='创新点'),
        ),
        migrations.AddField(
            model_name='project',
            name='personnumber',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='申报年度'),
        ),
        migrations.AddField(
            model_name='project',
            name='projectid',
            field=models.CharField(default='', max_length=45, verbose_name='项目编号'),
        ),
        migrations.AddField(
            model_name='project',
            name='selfbudget',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='自筹经费'),
        ),
        migrations.AddField(
            model_name='project',
            name='sort',
            field=models.CharField(default='', max_length=45, verbose_name='项目分类'),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='开始时间'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='项目状态'),
        ),
        migrations.AddField(
            model_name='project',
            name='totalbudget',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='总预算'),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.IntegerField(default=0, verbose_name='申报年度'),
        ),
        migrations.AlterField(
            model_name='project',
            name='applicant',
            field=models.CharField(default='', max_length=45, verbose_name='申报单位'),
        ),
        migrations.AlterField(
            model_name='project',
            name='apply_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='申请时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='complete_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='excution',
            field=models.TextField(default='', verbose_name='实施方式'),
        ),
        migrations.AlterField(
            model_name='project',
            name='leader',
            field=models.CharField(default='', max_length=10, verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='project',
            name='projectname',
            field=models.CharField(default='', max_length=45, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='purpose',
            field=models.TextField(default='', verbose_name='目的'),
        ),
    ]
