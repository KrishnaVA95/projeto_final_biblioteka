# Generated by Django 4.2.2 on 2023-07-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_loan_account_loan_copies'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='finalized_loan',
            field=models.BooleanField(default=False, null=True),
        ),
    ]