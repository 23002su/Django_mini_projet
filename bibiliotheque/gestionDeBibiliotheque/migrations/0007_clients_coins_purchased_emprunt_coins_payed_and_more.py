# Generated by Django 5.1.2 on 2025-01-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionDeBibiliotheque', '0006_rename_statu_livre_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='coins_purchased',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='emprunt',
            name='coins_payed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='livre',
            name='coins_to_pay',
            field=models.IntegerField(default=0),
        ),
    ]
