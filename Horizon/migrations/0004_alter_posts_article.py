# Generated by Django 5.0.4 on 2024-09-15 10:55

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Horizon', '0003_testimonials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='article',
            field=tinymce.models.HTMLField(),
        ),
    ]
