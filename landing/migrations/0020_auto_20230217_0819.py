# Generated by Django 2.2.13 on 2023-02-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0019_post_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contactus',
        ),
        migrations.RemoveField(
            model_name='post',
            name='codes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='inspiratinol',
        ),
        migrations.RemoveField(
            model_name='post',
            name='linkTab',
        ),
        migrations.RemoveField(
            model_name='post',
            name='with_code',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
