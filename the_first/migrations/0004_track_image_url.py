# Generated by Django 4.2.5 on 2023-10-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_first', '0003_track_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='image_url',
            field=models.CharField(default=''),
            preserve_default=False,
        ),
    ]
