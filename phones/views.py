from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', None)
    if sort == 'name':
        phone_object = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phone_object = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_object = Phone.objects.all().order_by('-price')
    else:
        phone_object = Phone.objects.all()

    context = {'phones': phone_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.all()
    for p in phone_object:
        s = p.slug
        if s == slug:
            print(p.name)
            context = {'phone': p}
    return render(request, template, context)


