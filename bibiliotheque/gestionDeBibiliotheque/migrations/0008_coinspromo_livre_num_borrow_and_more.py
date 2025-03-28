# Generated by Django 5.1.2 on 2025-01-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionDeBibiliotheque', '0007_clients_coins_purchased_emprunt_coins_payed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinsPromo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='livre',
            name='num_borrow',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clients',
            name='coins_purchased',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='livre',
            name='coins_to_pay',
            field=models.IntegerField(default=20),
        ),
    ]
