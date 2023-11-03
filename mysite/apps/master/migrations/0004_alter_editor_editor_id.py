# Generated by Django 4.2.4 on 2023-11-03 06:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_remove_editor_date_joined_remove_editor_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editor',
            name='editor_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
