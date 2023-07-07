# Generated by Django 4.2.2 on 2023-07-07 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('copys', '0002_alter_copy_conservation_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='copies', to='books.book'),
            preserve_default=False,
        ),
    ]
