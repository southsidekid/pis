from django.http import Http404
from django.shortcuts import render, redirect

from .models import Article


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist as exc:
        raise Http404 from exc


def create_post(request):
    # Проверка авторизации в стиле методички (адаптировано под Django 6)
    # В современных версиях is_anonymous — свойство, а не метод.
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                "title": request.POST.get("title", "").strip(),
                "text": request.POST.get("text", "").strip(),
            }

            if form["title"] and form["text"]:
                # проверка уникальности названия статьи
                if Article.objects.filter(title=form["title"]).exists():
                    form["errors"] = "Статья с таким названием уже существует"
                    return render(request, "create_post.html", {"form": form})

                article = Article.objects.create(
                    title=form["title"],
                    text=form["text"],
                    author=request.user,
                )
                return redirect("get_article", article_id=article.id)

            form["errors"] = "Не все поля заполнены"
            return render(request, "create_post.html", {"form": form})

        # метод GET — просто вернуть форму
        return render(request, "create_post.html", {})
    else:
        raise Http404
