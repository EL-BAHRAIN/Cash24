from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from .models import CustomerProfile, NextOfKin



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = (

            'first_name',
            'last_name',
            'gender',
            'address',
            'means_of_id',
            'customer_image',
            'phone',
            'email',
            'occupation',
        )

    def __init__(self, *args, **kwargs):
        super(CustomerProfileForm, self).__init__(*args, **kwargs)

        self.form_name = 'customer_form'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'gender',
            'address',
            'means_of_id',
            'customer_image',
            'phone',
            'email',
            'occupation',

            ButtonHolder(
                Submit('update bio data', 'Update bio data', css_class='btn-primary')
            )
        )


