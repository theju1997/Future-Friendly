# Generated by Django 4.2.7 on 2023-11-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thrill', '0003_rename_name_customer_data_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('ratings', models.IntegerField()),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='customer_data',
        ),
    ]
