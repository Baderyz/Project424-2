# Generated by Django 4.2 on 2023-06-06 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneStore', '0002_myuser_password1_myuser_password2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]