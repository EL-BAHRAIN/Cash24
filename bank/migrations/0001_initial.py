# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=50)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('means_of_id', models.ImageField(blank=True, upload_to='profile_image')),
                ('customer_image', models.ImageField(blank=True, upload_to='customer_image')),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=250)),
                ('occupation', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=50)),
                ('address', models.CharField(max_length=250, null=True)),
                ('phone', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('initiating_bank', models.CharField(choices=[('ACCESS BANK ', 'ACCESS BANK'), ('ECO BANK PLC', 'ECO BANK PLS'), ('FIDELITY BANK', 'FIDELITY BANK'), ('FIRST BANK', 'FIRST BANK'), ('FCMB', 'FCMB'), ('GT BANK', 'GT BANK'), ('HERITAGE BANK', 'HERITAGE BANK'), ('JAIZ BANK', 'JAIZ BANK'), ('KEYSTONE BANK', 'KEYSTONE BANK'), ('OCEANIC BANK', 'OCEANIC BANK'), ('SKYE BANK', 'SKYE BANK'), ('STANBIC IBTC BANK', 'STANBIC IBTC BANK'), ('STANDARD CHARTERED BANK', 'STANDARD CHARTERED BANK'), ('STERLING BANK', 'STERLING BANK'), ('UNION BANK', 'UNION BANK'), ('UBA', 'UBA'), ('UNITY BANK', 'UNITY BANK'), ('WEMA BANK', 'WEMA BANK'), ('ZENITH BANK', 'ZENITH BANK')], max_length=200)),
                ('initiating_account_number', models.CharField(default='', max_length=15)),
                ('name_of_sender', models.CharField(max_length=200)),
                ('transaction_type', models.CharField(choices=[('SEND', 'SEND'), ('RECEIVE', 'RECEIVE')], max_length=200)),
                ('means_of_transaction', models.CharField(choices=[('CASH', 'CASH'), ('POS', 'POS'), ('MOBILE_TRANSFER', 'MOBILE_TRANSFER'), ('BANK_CHEQUE', 'BANK_CHEQUE')], max_length=200)),
                ('beneficiary_bank', models.CharField(choices=[('ACCESS BANK ', 'ACCESS BANK'), ('ECO BANK PLC', 'ECO BANK PLS'), ('FIDELITY BANK', 'FIDELITY BANK'), ('FIRST BANK', 'FIRST BANK'), ('FCMB', 'FCMB'), ('GT BANK', 'GT BANK'), ('HERITAGE BANK', 'HERITAGE BANK'), ('JAIZ BANK', 'JAIZ BANK'), ('KEYSTONE BANK', 'KEYSTONE BANK'), ('OCEANIC BANK', 'OCEANIC BANK'), ('SKYE BANK', 'SKYE BANK'), ('STANBIC IBTC BANK', 'STANBIC IBTC BANK'), ('STANDARD CHARTERED BANK', 'STANDARD CHARTERED BANK'), ('STERLING BANK', 'STERLING BANK'), ('UNION BANK', 'UNION BANK'), ('UBA', 'UBA'), ('UNITY BANK', 'UNITY BANK'), ('WEMA BANK', 'WEMA BANK'), ('ZENITH BANK', 'ZENITH BANK')], max_length=200)),
                ('beneficiary_account_number', models.CharField(default='', max_length=15)),
                ('bank_charges', models.DecimalField(max_digits=7, decimal_places=2)),
                ('service_charge', models.DecimalField(max_digits=7, decimal_places=2)),
                ('transaction_amount', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
        ),
    ]
