import json
from http.client import HTTPResponse

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from shop.forms import ContactForm
from shop.models import OrderModel, ContactModel


def home(request):
    if request.method == 'GET':
        context = {
            'form': ContactForm,
        }
        info = ContactModel.objects.all()
        for i in info:
            if i.name == 'Контакт':
                context['contact'] = i.value
            if i.name == 'Реквизиты':
                context['pay'] = i.value
            if i.name == 'Адрес':
                context['address'] = i.value
            if i.name == 'Почта':
                context['email'] = i.value
        return render(request, 'html/index.html', context=context)
    if request.method == 'POST':
        print(1)
        form = ContactForm(request.POST or None)
        if form.is_valid():
            OrderModel.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            print(2)
        print(3)

        return HttpResponseRedirect('/#s5')


def about(request):
    return render(request, 'html/about.html')


def photos(request):
    return render(request, 'html/gallery.html')


def callback(request: HttpRequest):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['content']
    print(content)
    print(content)
    return render(request, 'html/index.html')
