# Generated by Django 4.2.4 on 2023-08-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_alter_employee_detail_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_detail',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee_detail',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee_detail',
            name='file',
            field=models.FileField(upload_to='file'),
        ),
        migrations.AlterField(
            model_name='employee_detail',
            name='skills',
            field=models.GenericIPAddressField(),
        ),
    ]
