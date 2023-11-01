from django .http import HttpResponse, HttpResponseNotFound, Http404
from django .shortcuts import render, redirect

from .forms import *
from .models import *

menu = [{'title': 'О сайте', 'url_name' : 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная свзяь','url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    posts = siteq.objects.all()
    cats = Category.objects.all()
    context = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cats':cats,'title': 'Главная страница', 'cat_selected': 0}
    return render(request, 'site1/index.html',context = context)

def about(request):
    return render(request, 'site1/about.html', {'title': 'О нас', 'menu': menu} )





def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена</h1>')



def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
           try:
               siteq.objects.create(**form.cleaned_data)
               return redirect('home')
           except:
               form.add_error(None, 'ошибка при добавлении формы')
    else:
        form = AddPostForm()
    posts = siteq.objects.all()
    cats = Category.objects.all()
    return render(request, 'site1/addpage.html', {'menu': menu, 'form': form, 'title': 'Добавление страницы', 'posts':posts, 'cats': cats})




def contact(request):
    return HttpResponse('Контакты наши')


def login(request):
    return HttpResponse('Авторизация')



def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, cat_id):
    posts = siteq.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context ={'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cats':cats, 'title': 'Главная страница', 'cat_selected': cat_id}
    return render(request, 'site1/index.html', context = context)