# Generated by Django 4.2.2 on 2023-07-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_merge_20230710_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishing_company',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]