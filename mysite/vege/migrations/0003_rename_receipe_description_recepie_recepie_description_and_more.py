# Generated by Django 5.2.1 on 2025-05-23 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_rename_receipe_recepie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recepie',
            old_name='receipe_description',
            new_name='recepie_description',
        ),
        migrations.RenameField(
            model_name='recepie',
            old_name='receipe_image',
            new_name='recepie_image',
        ),
        migrations.RenameField(
            model_name='recepie',
            old_name='receipe_name',
            new_name='recepie_name',
        ),
    ]
