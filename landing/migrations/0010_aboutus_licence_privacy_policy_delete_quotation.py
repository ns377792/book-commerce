# Generated by Django 4.1 on 2022-08-24 12:14

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_quotation_delete_aboutus_delete_licence_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='licence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_text', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Privacy_policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_text', tinymce.models.HTMLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Quotation',
        ),
    ]