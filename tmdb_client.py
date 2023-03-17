import requests

API_CODE = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNjY5ZGFkMjFmMjhlOTEwYzA1Mzk4NmM5NTBlNDFhZiIsInN1YiI6IjYzZjY4ZmM1ZDFjYTJhMDA3OWEwODBlYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Y8ZzfV81PknGRBDXKxabQZwQmgTZrM2Vo_6u9gL7fxA"


def header_returner():
    return {"Authorization": f"Bearer {API_CODE}"}


def endpoint_returner(words):
    return f"https://api.themoviedb.org/3/{words}"


def get_movies_list(list_name):
    response = requests.get(endpoint_returner(f"movie/{list_name}"), headers=header_returner())
    return response.json()


def get_single_movie(movie_id):
    response = requests.get(endpoint_returner(f"movie/{movie_id}"), headers=header_returner())
    return response.json()


def get_single_movie_cast(movie_id):
    response = requests.get(endpoint_returner(f"movie/{movie_id}/credits"), headers=header_returner())
    return response.json()["cast"]


def get_movie_images(movie_id):
    response = requests.get(endpoint_returner(f"movie/{movie_id}/images"), headers=header_returner())
    return response.json()


def get_series_airing():
    response = requests.get(endpoint_returner(f"tv/airing_today"), headers=header_returner())
    return response.json()["results"]


def search(search_query):
    response = requests.get(endpoint_returner(f"search/movie?query={search_query}"), headers=header_returner())
    return response.json()["results"]


def get_movies(how_many, list_name="popular"):
    #exception for: 'latest' nie posiada atrybutu results, poniewaz to lista tylko jednego filmu, wprowadzonego w baze jako ostatni.
    if list_name == "latest":
        data = [get_movies_list(list_name="latest")]
        return data
    data = get_movies_list(list_name)
    return data["results"][:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


# if __name__== "__main__":
#    data = get_movies()
#    print(data['results'][0])
