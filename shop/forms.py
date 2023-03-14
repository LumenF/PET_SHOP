from django import forms
from phonenumber_field.formfields import PhoneNumberField

from shop.models import OrderModel


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'yourclass', 'placeholder': 'Введіть імя',
                   }), label=u'Имя', max_length=255, required=True
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'yourclass', 'placeholder': '380 ',
                   }), label=u'Телефон', max_length=13, required=True
    )
    address = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'yourclass', 'placeholder': 'Введіть пошту',
                   }), label=u'Имя', max_length=255, required=True
    )

    class Meta:
        model = OrderModel