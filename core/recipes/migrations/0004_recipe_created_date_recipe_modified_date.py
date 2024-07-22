# Generated by Django 4.2 on 2023-05-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-23T21:11:16Z'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
