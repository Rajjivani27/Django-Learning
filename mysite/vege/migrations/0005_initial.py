# Generated by Django 5.2.1 on 2025-05-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vege', '0004_delete_recepie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recepie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepie_name', models.CharField(max_length=100)),
                ('recepie_description', models.TextField()),
                ('recepie_image', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
