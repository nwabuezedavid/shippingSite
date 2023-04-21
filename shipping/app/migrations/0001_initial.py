# Generated by Django 4.0.6 on 2022-11-19 17:40

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
            name='detailToship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShipperName', models.CharField(blank=True, max_length=50, null=True)),
                ('PhoneName', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('reciShipperName', models.CharField(blank=True, max_length=50, null=True)),
                ('recPhoneNumber', models.IntegerField(blank=True, null=True)),
                ('recEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('remark', models.CharField(blank=True, max_length=50, null=True)),
                ('typeofshipp', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('dateTime', models.DateTimeField()),
                ('courier', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenerateId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdCode', models.CharField(blank=True, max_length=50, null=True)),
                ('dateSend', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodsShipp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serialNumber', models.CharField(max_length=50)),
                ('BarIMage', models.ImageField(upload_to='barcode/')),
                ('dataShipped', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.detailtoship')),
            ],
        ),
        migrations.CreateModel(
            name='chattingcustmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
