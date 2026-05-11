from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist as exc:
        raise Http404 from exc

# path('article/new/', views.create_post, name='create_post'),

@login_required(login_url='/admin/login/')
# Вью для создания статьи. На GET возвращает форму, на POST — обрабатывает её
def create_post(request):
    if request.method == "POST":
        form = {
            "title": request.POST.get("title", "").strip(),
            "text": request.POST.get("text", "").strip(),
        }
        # проверяем, что оба поля заполнены
        if form["title"] and form["text"]:
            # проверка уникальности названия статьи
            if Article.objects.filter(title=form["title"]).exists():
                form["errors"] = "Статья с таким названием уже существует"
                return render(request, "create_post.html", {"form": form})
            
            # если всё ок, сохраняем статью и перенаправляем на её страницу
            article = Article.objects.create(
                title=form["title"],
                text=form["text"],
                author=request.user,
            )
            return redirect("get_article", article_id=article.id)
        
        # если не все поля заполнены, возвращаем форму с ошибкой
        form["errors"] = "Не все поля заполнены"
        return render(request, "create_post.html", {"form": form})

    # метод GET — просто вернуть форму
    return render(request, "create_post.html", {})

def register_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()

        if not username or not password or not email:
            error = 'Заполните все поля'
        else:
            try:
                User.objects.get(username=username)
                error = 'Пользователь с таким именем уже существует'
            except User.DoesNotExist:
                User.objects.create_user(username, email, password)
                return redirect('/login/')

    return render(request, 'register.html', {'error': error})


def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            error = 'Заполните все поля'
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error = 'Неверный логин или пароль'

    return render(request, 'login.html', {'error': error})
