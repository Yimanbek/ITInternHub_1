# Generated by Django 5.0.1 on 2024-02-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_comment_created_at_alter_news_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='links',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='news',
            name='place',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
