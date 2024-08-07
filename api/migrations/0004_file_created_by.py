# Generated by Django 4.2.13 on 2024-08-03 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_file_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='上传者'),
            preserve_default=False,
        ),
    ]
