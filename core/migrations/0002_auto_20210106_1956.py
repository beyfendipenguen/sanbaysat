# Generated by Django 3.1.5 on 2021-01-06 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bayi',
            name='bölge',
        ),
        migrations.RemoveField(
            model_name='bayi',
            name='posta_kodu',
        ),
    ]