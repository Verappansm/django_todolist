# Generated by Django 5.0.6 on 2024-06-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_updated_at_todo_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
