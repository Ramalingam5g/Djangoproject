# Generated by Django 3.2.5 on 2021-08-10 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bincardcreation', '0008_auto_20210810_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='Doc_no',
            new_name='Document_Number',
        ),
    ]