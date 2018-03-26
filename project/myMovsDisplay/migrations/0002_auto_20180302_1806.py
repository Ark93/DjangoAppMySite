# Generated by Django 2.0.2 on 2018-03-03 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myMovsDisplay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacciones',
            name='abono',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='cargo',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='transacciones',
            name='saldo',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6),
        ),
    ]