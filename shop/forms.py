from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'yourclass', 'placeholder': 'Введите имя',
                   }), label=u'Имя', max_length=255, required=True
    )
    phone = PhoneNumberField(
        widget=forms.TextInput(
            attrs={'class': 'yourclass', 'placeholder': '380 123456789',
                   }), label=u'Телефон', max_length=13, required=True
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'yourclass', 'placeholder': 'Ваш адрес',
                   }), label=u'Адрес', max_length=255, required=True
    )
