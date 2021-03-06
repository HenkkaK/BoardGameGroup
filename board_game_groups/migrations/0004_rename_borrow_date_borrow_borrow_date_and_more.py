# Generated by Django 4.0 on 2021-12-11 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_groups', '0003_borrow_contact_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow',
            old_name='Borrow_date',
            new_name='borrow_date',
        ),
        migrations.RenameField(
            model_name='borrow',
            old_name='Contact_information',
            new_name='contact_information',
        ),
        migrations.RenameField(
            model_name='borrow',
            old_name='Borrowed_Game',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='borrow',
            old_name='Planned_return_date',
            new_name='planned_return_date',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='Game_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='Game_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='Owner',
            new_name='owner',
        ),
    ]
