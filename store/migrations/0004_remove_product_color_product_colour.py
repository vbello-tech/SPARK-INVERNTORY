# Generated by Django 5.2.4 on 2025-07-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_colour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.ManyToManyField(to='store.colour'),
        ),
    ]
