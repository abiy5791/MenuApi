# Generated by Django 4.2.3 on 2023-07-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.TextField()),
                ('cat_image', models.TextField()),
                ('cat_desc', models.TextField()),
                ('updated_in', models.DateTimeField(auto_now=True)),
                ('created_in', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
