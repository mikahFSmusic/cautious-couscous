# Generated by Django 3.1.1 on 2020-09-20 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Hotel',
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'ordering': ('-created_at',), 'verbose_name': 'hotel', 'verbose_name_plural': 'hotels'},
        ),
    ]