# Generated by Django 4.2.2 on 2024-12-14 16:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0004_alter_product_options_product_publication_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": [
                    "name",
                    "purchase_price",
                    "created_at",
                    "publication_status",
                ],
                "permissions": [
                    ("can_unpublish_product", "Can unpublish product"),
                    ("can_delete_product", "Can delete product"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите пользователя продукта",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="publication_status",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
    ]
