# Generated by Django 4.2 on 2024-01-13 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_alter_question_answer3_alter_question_answer4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='heading',
        ),
    ]
