# Generated by Django 3.2.8 on 2021-10-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_deposit_deposit_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.IntegerField(default=5000, null=True),
        ),
    ]
