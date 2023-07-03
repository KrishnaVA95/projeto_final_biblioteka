# Generated by Django 4.2.2 on 2023-07-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField(auto_now_add=True)),
                ('overdue', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]