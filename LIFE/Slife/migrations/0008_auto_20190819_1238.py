# Generated by Django 2.2.1 on 2019-08-19 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Slife', '0007_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('can vote once ', 'can view vote'),)},
        ),
    ]