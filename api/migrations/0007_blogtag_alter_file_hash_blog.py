# Generated by Django 4.2.13 on 2024-08-05 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='标签名称')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.AlterField(
            model_name='file',
            name='hash',
            field=models.CharField(max_length=255, unique=True, verbose_name='哈希'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.TextField(max_length=255, verbose_name='标题')),
                ('content', models.TextField(max_length=16777215, verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后一次更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('tags', models.ManyToManyField(to='api.blogtag', verbose_name='标签')),
            ],
            options={
                'permissions': [('blog', 'Can control blog.')],
            },
        ),
    ]
