# Generated by Django 3.2.5 on 2021-08-18 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincardcreation', '0002_alter_material_material_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='Verification_Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
