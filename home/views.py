from django.shortcuts import render
from .models import News, Publications, Talks, Articles

# Create your views here.
def home(request):
    """View function for home page of site."""

    context = {
        'news': News.objects.order_by("-date")[:5],
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'home.html', context=context)


def research(request):
    """View function for research page of site."""

    context = {
        'publications': Publications.objects.order_by("-date"),
        'talks': Talks.objects.order_by("-date"),
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'research.html', context=context)


def blog(request):
    """View function for blog page of site."""

    context = {
        'articles': Articles.objects.order_by("-date")
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'blog.html', context=context)

from django.http import Http404


def article(request, url_name):
    """Returns a view to an Article."""
    try:
        art = Articles.objects.get(url_name=url_name)
    except Articles.DoesNotExist:
        raise Http404('Article does not exist !')

    context = {'article': art}

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'article.html', context=context)
