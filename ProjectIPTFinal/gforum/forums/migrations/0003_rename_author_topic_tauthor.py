# Generated by Django 4.2 on 2023-05-08 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_remove_topic_tauthor_topic_author_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='author',
            new_name='tauthor',
        ),
    ]
