# Generated by Django 4.0.2 on 2022-09-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttag',
            old_name='caption',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_delete',
            field=models.BooleanField(null=True, verbose_name='حذف شده/حذف نشده'),
        ),
    ]
