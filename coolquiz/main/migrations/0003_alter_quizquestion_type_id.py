# Generated by Django 4.0.3 on 2022-04-08 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_quizquestion_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='type_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.quiztype'),
        ),
    ]
