# Generated by Django 4.0.6 on 2022-07-10 13:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
