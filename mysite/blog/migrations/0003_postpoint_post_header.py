# Generated by Django 5.1.3 on 2025-01-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_postpoint_post_images_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpoint',
            name='post_header',
            field=models.CharField(default='HEADER', max_length=250),
        ),
    ]
