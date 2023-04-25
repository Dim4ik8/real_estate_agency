# Generated by Django 2.2.24 on 2023-04-25 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20230425_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Flat', verbose_name='Квартира, на которую пожаловались')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Кто жалуется')),
            ],
        ),
    ]
