# Generated by Django 4.0.5 on 2022-08-01 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppDiario', '0010_posteo_descripcion_alter_posteo_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
