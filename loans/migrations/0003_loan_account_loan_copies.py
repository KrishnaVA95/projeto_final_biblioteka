# Generated by Django 4.2.2 on 2023-07-07 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('copys', '0003_copy_book'),
        ('loans', '0002_alter_loan_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='account',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='loans', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='copies',
            field=models.ManyToManyField(related_name='loans', to='copys.copy'),
        ),
    ]