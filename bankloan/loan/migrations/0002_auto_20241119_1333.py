# Generated by Django 3.2.25 on 2024-11-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=30)),
                ('loan_amnt', models.FloatField()),
                ('cust_acntno', models.IntegerField()),
                ('cust_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='BankLoan',
        ),
    ]
