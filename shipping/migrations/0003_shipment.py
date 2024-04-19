# Generated by Django 4.2 on 2024-04-19 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipping', '0002_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_contactnumber', models.IntegerField()),
                ('sender_city', models.CharField(max_length=100)),
                ('sender_postalcode', models.IntegerField()),
                ('sender_telephone1', models.IntegerField()),
                ('sender_telephone2', models.IntegerField(null=True)),
                ('sender_address', models.CharField(max_length=100)),
                ('reciever_firstname', models.CharField(max_length=100)),
                ('reciever_lastname', models.CharField(max_length=100)),
                ('reciever_contactnumber', models.IntegerField()),
                ('reciever_email', models.EmailField(max_length=254)),
                ('reciever_city', models.CharField(max_length=100)),
                ('reciever_postalcode', models.IntegerField()),
                ('reciever_telephone1', models.IntegerField()),
                ('reciever_telephone2', models.IntegerField(null=True)),
                ('reciever_address', models.CharField(max_length=100)),
                ('reciever_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever_country', to='shipping.country')),
                ('sender_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_country', to='shipping.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]