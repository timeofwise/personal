# Generated by Django 3.2.8 on 2021-10-31 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_deposit_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='deposit_account',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='home.account'),
        ),
    ]
