# Generated by Django 4.0 on 2021-12-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('board_game_groups', '0008_alter_game_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='contact_information',
        ),
        migrations.AddField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
