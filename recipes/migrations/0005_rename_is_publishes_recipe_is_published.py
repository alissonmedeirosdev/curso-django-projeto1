# Generated by Django 5.1.4 on 2025-01-29 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_rename_category_recipe_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='is_publishes',
            new_name='is_published',
        ),
    ]
