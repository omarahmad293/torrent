import requests
import urllib.parse


API_KEY = '9fafa6282710f17c0956691d1d6ac16a'
main_api = "https://api.themoviedb.org/3/"

'''
Search results  are in data['results'] as a list, iterate using:
for result in data['results']
result is a dict
'''


def search(search):

    # https://api.themoviedb.org/3/search/multi?api_key=9fafa6282710f17c0956691d1d6ac16a&query=avengers

    url = main_api + 'search/' + 'multi?' + \
        urllib.parse.urlencode({'api_key': API_KEY, 'query': search})
    response = requests.get(url)
    data = response.json()
    return data


def find_imdb(imdb_id):
    '''
    Takes in IMDb ID and returns JSON
    '''
    # https://api.themoviedb.org/3/find/tt0182576?api_key=9fafa6282710f17c0956691d1d6ac16a&external_source=imdb_id

    url = main_api + 'find/' + str(imdb_id) + '?' + urllib.parse.urlencode(
        {'api_key': API_KEY, 'external_source': 'imdb_id'})
    response = requests.get(url)
    data = response.json()
    return data


def view_results(data):
    '''
    Takes in data as a JSON object (dictionary) and returns the title or name
    '''
    for result in data['results']:
        if result['media_type'] == 'movie':
            print(result['title'])  # for movies
        elif result['media_type'] == 'tv' or result['media_type'] == 'person':
            print(result['name'])


def view_details(media_type, media_id):
    '''
    Takes in media type ('tv', 'movie', ...) and returns JSON
    '''
    # https://api.themoviedb.org/3/movie/671?api_key=9fafa6282710f17c0956691d1d6ac16a

    url = main_api + media_type + '/' + \
        str(media_id) + '?' + urllib.parse.urlencode({'api_key': API_KEY})
    response = requests.get(url)
    data = response.json()
    return data
