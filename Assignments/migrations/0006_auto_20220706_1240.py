# Generated by Django 3.2.8 on 2022-07-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignments', '0005_auto_20220706_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='interpreter_payment',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='address',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='company',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='flat_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='hourly_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='interpreter',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='language',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='mileage_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='miles',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='parking',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='patient',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='po_num',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='type',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
    ]
