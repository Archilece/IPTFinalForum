# Generated by Django 4.2 on 2023-05-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_rename_author_topic_tauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forums.topic'),
        ),
    ]