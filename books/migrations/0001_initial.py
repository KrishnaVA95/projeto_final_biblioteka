# Generated by Django 4.2.2 on 2023-07-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('author', models.CharField(max_length=127)),
                ('number_page', models.IntegerField()),
                ('description', models.TextField()),
                ('cover', models.CharField(max_length=255)),
                ('published', models.IntegerField()),
                ('number_copy', models.IntegerField()),
                ('copies_available', models.IntegerField()),
            ],
        ),
    ]