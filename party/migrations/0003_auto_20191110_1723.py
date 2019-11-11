# Generated by Django 2.0.2 on 2019-11-10 17:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_auto_20191029_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='charisma',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='base',
            name='con',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='base',
            name='dex',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='base',
            name='intel',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='base',
            name='max_hp',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)]),
        ),
        migrations.AlterField(
            model_name='base',
            name='strengh',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='base',
            name='wisdom',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
    ]
