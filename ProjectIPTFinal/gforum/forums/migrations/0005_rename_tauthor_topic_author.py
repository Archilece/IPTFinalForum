# Generated by Django 4.2 on 2023-05-08 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0004_rename_author_comment_cauthor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='tauthor',
            new_name='author',
        ),
    ]
