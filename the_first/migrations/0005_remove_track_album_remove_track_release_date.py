# Generated by Django 4.2.5 on 2023-10-08 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_first', '0004_track_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.RemoveField(
            model_name='track',
            name='release_date',
        ),
    ]
