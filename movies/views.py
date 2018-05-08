from django.http import Http404
from django.shortcuts import render
from .models import Movie


def index(request):

    all_movies = Movie.objects.all()
    context = {'all_movies': all_movies}
    return render(request, 'movies/movies.html', context)


def detail(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/detail.html', {'movie': movie})
