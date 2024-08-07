# Generated by Django 4.2.13 on 2024-08-03 12:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_file_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='hash',
            field=models.CharField(default=0, max_length=256, verbose_name='哈希'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='文件名'),
        ),
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
