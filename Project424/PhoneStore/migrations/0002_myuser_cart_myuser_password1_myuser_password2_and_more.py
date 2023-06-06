# Generated by Django 4.2 on 2023-06-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='cart', to='PhoneStore.phone'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='password1',
            field=models.CharField(default=12345678, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='password2',
            field=models.CharField(default=12345678, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]