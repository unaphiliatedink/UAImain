# Generated by Django 4.1.2 on 2023-01-04 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_announcement_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='status',
            field=models.CharField(choices=[('DISABLED', 'DISABLED'), ('ACTIVE', 'ACTIVE')], default='DISABLED', max_length=10),
        ),
    ]