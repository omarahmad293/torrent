import requests
from bs4 import BeautifulSoup
from tmdb_api import view_details


def get_data(movie_id):
    '''
    Takes in movie ID and returns a list with name and year
    '''

    movie_data = []

    data = view_details('movie', movie_id)

    for word in data['title'].split():
        movie_data.append(word)

    movie_data.append(data['release_date'].split('-')[0])

    return movie_data


def get_links(movie_id):
    '''
    Takes in a list containing movie name and year.
    Example: ['Black', 'Panther', '2018']

    Returns a list of magnet links.
    '''

    movie_data = get_data(movie_id)

    links = []
    movie = 'https://1337x.to/movie/' + str(movie_id) + '/'

    for word in movie_data:
        movie += str(word) + '-'

    movie = movie[:-1] + '/'

    r = requests.get(movie)
    soup = BeautifulSoup(r.content, "html.parser")

    items = soup.findAll("td", {"class": "coll-1 name"})
    for item in items:
        if item.a['href'] == "/sub/70/0/":
            links.append(item.findAll('a')[1]['href'])

    return links
