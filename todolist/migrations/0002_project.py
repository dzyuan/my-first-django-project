# Generated by Django 2.2.1 on 2019-07-11 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=45)),
                ('danwei', models.CharField(max_length=45)),
                ('leader', models.CharField(max_length=10)),
                ('cost', models.FloatField()),
            ],
        ),
    ]
