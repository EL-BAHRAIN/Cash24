from django.db import models


# Create your models here.

GENDER_TYPE =(
    ('MALE', 'MALE'),
    ( 'FEMALE', 'FEMALE')
)

MEANS_OF_TRANSACTION = (
    ('CASH', 'CASH'),
    ('POS', 'POS'),
    ('MOBILE_TRANSFER', 'MOBILE_TRANSFER'),
    ('BANK_CHEQUE', 'BANK_CHEQUE')

)


TRANSACTION_TYPE = (
    ('SEND', 'SEND'),
    ('RECEIVE', 'RECEIVE')
)
BANKS = (
    ('ACCESS BANK ', 'ACCESS BANK'),
    ('ECO BANK PLC', 'ECO BANK PLS'),
    ('FIDELITY BANK', 'FIDELITY BANK'),
    ('FIRST BANK', 'FIRST BANK'),
    ('FCMB', 'FCMB'),
    ('GT BANK', 'GT BANK'),
    ('HERITAGE BANK', 'HERITAGE BANK'),
    ('JAIZ BANK', 'JAIZ BANK'),
    ('KEYSTONE BANK', 'KEYSTONE BANK'),
    ('OCEANIC BANK', 'OCEANIC BANK'),
    ('SKYE BANK', 'SKYE BANK'),
    ('STANBIC IBTC BANK', 'STANBIC IBTC BANK'),
    ('STANDARD CHARTERED BANK', 'STANDARD CHARTERED BANK'),
    ('STERLING BANK', 'STERLING BANK'),
    ('UNION BANK', 'UNION BANK'),
    ('UBA', 'UBA'),
    ('UNITY BANK', 'UNITY BANK'),
    ('WEMA BANK', 'WEMA BANK'),
    ('ZENITH BANK', 'ZENITH BANK')
)


class CustomerProfile(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE)
    address = models.CharField(max_length=250, blank=True)
    means_of_id = models.ImageField(upload_to='profile_image', blank=True)
    customer_image = models.ImageField(upload_to='customer_image', blank=True)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=250)
    occupation = models.CharField(max_length=250)




class NextOfKin(models.Model):
    # referrer = models.OneToOneField(CustomerProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE)
    address = models.CharField(max_length=250, null=True)
    phone = models.IntegerField(default=0)



class Transaction(models.Model):
    initiating_bank = models.CharField(max_length=200, choices=BANKS)
    initiating_account_number = models.CharField(max_length=15, default='')
    name_of_sender = models.CharField(max_length=200)
    transaction_type = models.CharField(max_length=200, choices=TRANSACTION_TYPE)
    means_of_transaction = models.CharField(max_length=200, choices=MEANS_OF_TRANSACTION)
    beneficiary_bank = models.CharField(max_length=200, choices=BANKS)
    beneficiary_account_number = models.CharField(max_length=15, default='')
    bank_charges = models.DecimalField(max_digits=7, decimal_places=2)
    service_charge = models.DecimalField(max_digits=7, decimal_places=2)
    transaction_amount = models.DecimalField(max_digits=7, decimal_places=2)
