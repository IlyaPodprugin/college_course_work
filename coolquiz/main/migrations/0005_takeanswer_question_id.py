# Generated by Django 4.0.3 on 2022-05-27 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_quizanswer_question_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeanswer',
            name='question_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.quizquestion'),
        ),
    ]
