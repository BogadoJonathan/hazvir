# Generated by Django 4.1.7 on 2023-02-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
