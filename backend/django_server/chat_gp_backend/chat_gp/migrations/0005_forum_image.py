# Generated by Django 4.2.3 on 2024-03-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat_gp", "0004_category_description_category_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="forum",
            name="image",
            field=models.CharField(
                default="https://www.shutterstock.com/image-vector/default-ui-image-placeholder-wireframes-600nw-1037719192.jpg",
                max_length=500,
            ),
            preserve_default=False,
        ),
    ]
