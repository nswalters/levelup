# Generated by Django 3.1.3 on 2020-11-25 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_auto_20201124_0042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='gametype',
            new_name='gameTypeId',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='number_of_players',
            new_name='numberOfPlayers',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='skill_level',
            new_name='skillLevel',
        ),
        migrations.RemoveField(
            model_name='game',
            name='gamer',
        ),
    ]
