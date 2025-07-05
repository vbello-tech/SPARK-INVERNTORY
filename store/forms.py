from django import forms
from .models import ProductCategory, Colour
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from phonenumber_field.formfields import PhoneNumberField


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('category', 'quantity')

        widgets = {
            'category': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'NAME OF THE CATEGORIES',
                }
            ),
            'quantity': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'QUANTITY OF THE CATEGORIES',
                }
            ),
        }


class AddProductForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'NAME OF THE PHONE',
    }))

    color = forms.ModelMultipleChoiceField(required=False,
                                           queryset=Colour.objects.all(),
                                           widget=forms.TextInput(attrs={
                                               'class': 'form-control',
                                               "placeholder": 'COLOR OF THE PHONE',
                                           }))

    type = forms.ModelChoiceField(required=False,
                                  queryset=ProductCategory.objects.all(),
                                  widget=forms.Select(attrs={
                                      'class': 'form-control bootstrap-select',
                                  }))

    serial_no = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        "placeholder": 'IMEI NUMBER OF THE PHONE',
    }))

    spec = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'RAM AND ROM OF THE PHONE',
    }))

    quantity = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        "placeholder": 'IMEI NUMBER OF THE PHONE',
    }))


class CheckOutForm(forms.Form):
    buyer = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "INPUT BUYER'S NAME",
    }))
    phone = PhoneNumberField(region="CA", widget=RegionalPhoneNumberWidget(attrs={
        'class': 'form-control',
        'placeholder': "INPUT BUYER'S PHONE NUMBER",
    }))
