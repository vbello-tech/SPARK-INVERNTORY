from django import forms
from .models import ProductCategory, Colour, Product
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from phonenumber_field.formfields import PhoneNumberField


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('category', )

        widgets = {
            'category': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'NAME OF THE CATEGORIES',
                }
            ),
            # 'quantity': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         "placeholder": 'QUANTITY OF THE CATEGORIES',
            #     }
            # ),
        }


class AddColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ('colour', )

        widgets = {
            'colour': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Add a Colour',
                }
            ),
        }


Type_Choice = [
    ('Used', 'Used'),
    ('UK', 'UK'),
    ('China', 'China'),
]


class AddProductForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'NAME OF THE PHONE',
    }))

    color = forms.ModelMultipleChoiceField(required=False,
                                           queryset=Colour.objects.all(),
                                           widget=forms.SelectMultiple(attrs={
                                               'class': 'form-control',
                                               "placeholder": 'COLOR OF THE PHONE',
                                           }))

    category = forms.ModelChoiceField(required=False,
                                  queryset=ProductCategory.objects.all(),
                                  widget=forms.Select(attrs={
                                      'class': 'form-control bootstrap-select',
                                  }))

    serial_no = forms.IntegerField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'IMEI NUMBER OF THE PHONE',
    }))

    ram = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'RAM',
    }))

    rom = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": 'ROM ',
    }))

    quantity = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        "placeholder": 'Quantity of the Phone',
    }))

    type = forms.ChoiceField(required=False,
                             choices=Type_Choice,
                             widget=forms.Select(attrs={
                                 'class': 'form-control bootstrap-select',
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
