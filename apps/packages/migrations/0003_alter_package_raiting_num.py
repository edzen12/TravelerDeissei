# Generated by Django 4.1.7 on 2023-03-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_alter_package_raiting_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='raiting_num',
            field=models.SmallIntegerField(max_length=5, verbose_name='Рейтинг'),
        ),
    ]
