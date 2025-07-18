# Generated by Django 5.2.4 on 2025-07-07 16:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_contactmessage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='sayed', upload_to='services/', verbose_name='صورة الخدمة'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_ar',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='الوصف'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_ar',
            field=models.CharField(max_length=200, null=True, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='العنوان'),
        ),
    ]
