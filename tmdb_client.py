import requests
import random

api_code = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNjY5ZGFkMjFmMjhlOTEwYzA1Mzk4NmM5NTBlNDFhZiIsInN1YiI6IjYzZjY4ZmM1ZDFjYTJhMDA3OWEwODBlYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Y8ZzfV81PknGRBDXKxabQZwQmgTZrM2Vo_6u9gL7fxA"


def get_authorized_dict():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = api_code
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_name):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    api_token = api_code
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_movies(how_many, list_name="popular"):
    if list_name == "latest":
        data = [get_movies_list(list_name="latest")]
        return data
    data = get_movies_list(list_name)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = api_code
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = api_code
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    api_token = api_code
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_series_airing():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    api_token = api_code
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()["results"]


def search(search_query):
    base_url = "https://api.themoviedb.org/3/"
    api_token = api_code
    headers = {"Authorization": f"Bearer {api_token}"}
    endpoint = f"{base_url}search/movie?query={search_query}"
    # endpoint = f"{base_url}search/movie?api_key={api_key}&query={search_query}"

    response = requests.get(endpoint, headers=headers)
    return response.json()["results"]


# if __name__== "__main__":
#    data = get_movies()
#    print(data['results'][0])
