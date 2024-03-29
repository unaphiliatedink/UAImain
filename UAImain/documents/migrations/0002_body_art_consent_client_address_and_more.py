# Generated by Django 4.1.2 on 2023-03-27 13:06

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='body_art_consent',
            name='client_address',
            field=models.CharField(default='add address', max_length=255),
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='client_drivers_license',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='client_email',
            field=models.EmailField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='client_emergency_contact',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='client_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='client_phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact number', max_length=31),
        ),
    ]
