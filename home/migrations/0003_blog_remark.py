# Generated by Django 4.1.4 on 2023-01-26 07:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='remark',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
