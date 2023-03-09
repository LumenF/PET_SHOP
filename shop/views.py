import json
from http.client import HTTPResponse

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from shop.forms import ContactForm
from shop.models import OrderModel


class IndexView(FormView):
    template_name = 'html/index.html'
    form_class = ContactForm
    success_url = '/'


def home(request):
    if request.method == 'GET':
        return render(request, 'html/index.html', context={'form': ContactForm})
    if request.method == 'POST':

        form = ContactForm(request.POST or None)
        if form.is_valid():

            OrderModel.objects.create(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
        return HttpResponseRedirect('/#s4')


def about(request):
    return render(request, 'html/about.html')


def photos(request):
    return render(request, 'html/gallery.html')


def callback(request: HttpRequest):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['content']
    print(content)
    return render(request, 'html/index.html')
