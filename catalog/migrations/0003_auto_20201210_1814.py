# Generated by Django 3.1.3 on 2020-12-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_result_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='level',
            field=models.CharField(max_length=50),
        ),
    ]
