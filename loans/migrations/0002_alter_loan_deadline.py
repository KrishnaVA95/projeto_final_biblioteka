# Generated by Django 4.2.2 on 2023-07-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
