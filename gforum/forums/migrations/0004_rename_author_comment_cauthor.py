# Generated by Django 4.2 on 2023-05-08 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_rename_author_topic_tauthor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='cauthor',
        ),
    ]
