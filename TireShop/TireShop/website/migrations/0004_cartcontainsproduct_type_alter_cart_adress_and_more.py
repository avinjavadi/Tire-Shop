# Generated by Django 4.1 on 2023-01-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_rim_pattern_tube_layer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartcontainsproduct',
            name='type',
            field=models.CharField(default='tire', max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='adress',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='cart',
            name='datetime',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='postcode',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
