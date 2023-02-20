# Generated by Django 4.1 on 2022-09-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_remove_category_with_code_post_with_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='bootstrap',
        ),
        migrations.RemoveField(
            model_name='category',
            name='dark',
        ),
        migrations.RemoveField(
            model_name='category',
            name='hcj',
        ),
        migrations.RemoveField(
            model_name='category',
            name='light',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tailwind',
        ),
        migrations.RemoveField(
            model_name='category',
            name='without_code',
        ),
        migrations.AddField(
            model_name='post',
            name='inspiratinol',
            field=models.BooleanField(default=False),
        ),
    ]
