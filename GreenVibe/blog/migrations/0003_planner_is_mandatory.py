# Generated by Django 4.2 on 2023-12-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_planner_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='is_mandatory',
            field=models.BooleanField(default=False),
        ),
    ]
