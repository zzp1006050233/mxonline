# Generated by Django 2.0.1 on 2018-01-09 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6)),
                ('mobile', models.CharField(max_length=11, null=True)),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
            ],
        ),
    ]
