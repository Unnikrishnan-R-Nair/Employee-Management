# Generated by Django 5.0.1 on 2024-02-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_employeedetails_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], default='Active', max_length=100),
        ),
    ]
