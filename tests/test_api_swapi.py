"""
Placeholder
"""
import requests

SWAPI_API = 'https://swapi.co/api/'


def swapi_films(episode):
	"""
	Gets the films listed in the api.
	:param episode:
	:return: response json
	"""
	response = requests.get(SWAPI_API + 'films/' + str(episode))
	return response


def swapi_film_code(episode):
	"""
	Asserts that a 200 was returned
	:param episode:
	"""
	assert swapi_films(episode).status_code == 200


def swapi_films_episode(name, episode):
	"""
	This checks that all the films are in the response.
	:param name:
	:param episode:
	"""
	assert name.lower() == swapi_films(episode).json()['title'].lower()


def test_episode_1():
	"""
	This runs through episode 1.
	"""
	swapi_film_code(1)
	swapi_films_episode('A New Hope', 1)


def test_episode_2():
	"""
	This runs through episode 2.
	"""
	swapi_film_code(2)
	swapi_films_episode('The Empire Strikes Back', 2)


def test_episode_3():
	"""
	This runs through episode 3.
	"""
	swapi_film_code(3)
	swapi_films_episode('Return of the Jedi', 3)


def test_episode_4():
	"""
	This runs through episode 4.
	"""
	swapi_film_code(4)
	swapi_films_episode('The Phantom Menace', 4)


def test_episode_5():
	"""
	This runs through episode 5.
	"""
	swapi_film_code(5)
	swapi_films_episode('Attack of the Clones', 5)


def test_episode_6():
	"""
	This runs through episode 6.
	"""
	swapi_film_code(6)
	swapi_films_episode('Revenge of the Sith', 6)


def test_episode_7():
	"""
	This runs through episode 7.
	"""
	swapi_film_code(7)
	swapi_films_episode('The Force Awakens', 7)


def test_episode_8():
	"""
	This runs through episode 8.
	"""
	swapi_film_code(8)
	swapi_films_episode('The Last Jedi', 8)


def test_episode_9():
	"""
	This runs through episode 9.
	"""
	swapi_film_code(9)
	swapi_films_episode('The Rise of Skywalker', 9)
