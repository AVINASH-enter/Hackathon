# Generated by Django 5.1.1 on 2024-09-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.CharField(max_length=100),
        ),
    ]