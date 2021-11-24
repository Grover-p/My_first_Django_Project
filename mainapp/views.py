from django.shortcuts import render

# Create your views here.


def index(request):
    content = {'title':'Магазин'}
    return render(request, "mainapp/index.html", content)

def products(request):
    return render(request, "mainapp/products.html")

def contact(request):
    return render(request, "mainapp/contact.html")

def context(request):
    context = {
        'title':'test context',
        'header':'Добро пожаловать на сайт',
        'username':'Джон',
    }
    return render(request, "mainapp/contact.html", context)


def menu_product(request):
    links_menu = [
        {'href':'products_all', 'name':'Всё'},
        {'href':'products_home', 'name':'Дом'},
        {'href':'products_office', 'name':'Офис'},
        {'href':'products_modern', 'name':'Модерн'},
        {'href':'products_classic', 'name':'Классика'}
    ]
    return render(request, 'mainapp/products.html', links_menu)