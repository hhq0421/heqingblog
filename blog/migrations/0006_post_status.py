# Generated by Django 4.2.7 on 2023-11-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_posts_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
