# Generated by Django 2.1.2 on 2018-10-29 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ori_url', models.ImageField(upload_to='OriImg')),
                ('png_url', models.ImageField(upload_to='PngImg')),
            ],
        ),
    ]
