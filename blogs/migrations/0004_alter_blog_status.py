# Generated by Django 5.0 on 2023-12-06 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_rename_auther_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft'),
        ),
    ]
