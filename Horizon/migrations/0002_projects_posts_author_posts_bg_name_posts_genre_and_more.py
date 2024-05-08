# Generated by Django 4.2.7 on 2024-04-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Horizon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=200)),
                ('type_proj', models.CharField(max_length=50)),
                ('live', models.BooleanField(default=False)),
                ('tech_used', models.CharField(max_length=100)),
                ('bg_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='Caspian', max_length=50),
        ),
        migrations.AddField(
            model_name='posts',
            name='bg_name',
            field=models.CharField(default='grass.jpg', max_length=100),
        ),
        migrations.AddField(
            model_name='posts',
            name='genre',
            field=models.CharField(default='Essay', max_length=30),
        ),
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='sub_title',
            field=models.CharField(default='Short subtitle', max_length=200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(default='Add your title', max_length=100),
        ),
    ]