# Generated by Django 4.2 on 2023-06-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneStore', '0003_delete_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='cart', to='PhoneStore.phone'),
        ),
    ]
