# Generated by Django 5.2.3 on 2025-07-06 18:53

import ckeditor_uploader.fields
import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content2',
            field=markdownx.models.MarkdownxField(null=True, verbose_name='md內容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='html內容'),
        ),
    ]
