# Generated by Django 4.0.3 on 2022-05-30 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_take_percent_efficiency_take_total_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='take',
            old_name='total',
            new_name='total_score',
        ),
        migrations.RenameField(
            model_name='take',
            old_name='score',
            new_name='user_score',
        ),
    ]