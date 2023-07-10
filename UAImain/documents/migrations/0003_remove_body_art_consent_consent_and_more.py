# Generated by Django 4.1.2 on 2023-03-30 02:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_body_art_consent_client_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='body_art_consent',
            name='consent',
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='allergies',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='client_date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='consent_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='date_signed',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='medical_conditions',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='medications',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='pregnancy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='skin_conditions',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='tattoo_design',
            field=models.CharField(default='dragon tattoo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='tattoo_placement',
            field=models.CharField(default='forearm', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='body_art_consent',
            name='tattoo_size',
            field=models.CharField(default='1ft', max_length=100),
            preserve_default=False,
        ),
    ]