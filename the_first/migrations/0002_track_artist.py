# Generated by Django 4.2.5 on 2023-09-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.CharField(default=''),
            preserve_default=False,
        ),
    ]
