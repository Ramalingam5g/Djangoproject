# Generated by Django 3.2.5 on 2021-09-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bincardcreation', '0003_auto_20210818_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='Transaction_Type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterModelTable(
            name='materialsinventory',
            table=None,
        ),
    ]