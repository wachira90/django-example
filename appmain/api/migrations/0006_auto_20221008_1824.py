# Generated by Django 3.2.16 on 2022-10-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20221008_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(default=0, max_length=100),
        ),
    ]