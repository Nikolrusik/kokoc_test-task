# Generated by Django 4.1.7 on 2023-03-10 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name color')),
                ('type', models.CharField(choices=[('BORDER', 'Border color'), ('BACKGROUND', 'Profile background')], default='BORDER', max_length=100, verbose_name='Type item')),
                ('color', models.CharField(max_length=100, verbose_name='Color')),
                ('price', models.FloatField(default=0.0, verbose_name='Item price')),
            ],
        ),
        migrations.CreateModel(
            name='UserItemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BORDER', 'Border color'), ('BACKGROUND', 'Profile background')], default='BORDER', max_length=100, verbose_name='Type item')),
                ('color', models.CharField(max_length=100, verbose_name='Color')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopapp.shopitemsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
