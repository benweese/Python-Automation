"""
Placeholder
"""
import requests

SWAPI_API = 'https://swapi.co/api/'


def swapi_films():
	"""
	Gets the films listed in the api.
	:return: response json
	"""
	response = requests.get(SWAPI_API + 'films/')
	return response


def swapi_film_code():
	"""
	Asserts that a 200 was returned
	"""
	assert swapi_films().status_code == 200


def swapi_films_episode_4():
	"""
	This checks that all the films are in the response.
	"""
	json = swapi_films().json()
	assert 'A New Hope' == json[]
