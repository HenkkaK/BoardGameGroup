# Generated by Django 4.0 on 2021-12-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_groups', '0005_remove_game_is_borrowed_borrow_is_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='is_borrowed',
            field=models.BooleanField(default=False),
        ),
    ]