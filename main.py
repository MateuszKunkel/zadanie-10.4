from flask import Flask, flash, render_template, request, url_for, redirect
from faker import Faker
import tmdb_client
import datetime

fake = Faker()
app = Flask(__name__)

FAVORITES = set()
#OPTIONS: list of all possible genres in homepage menu buttons
OPTIONS = ["Latest", "Now playing", "Popular", "Top rated", "Upcoming"]

app.secret_key = "asdhjrzkjwe"


@app.route("/favorites/add", methods=["POST"])
def add_to_favorites():
    movie_id = request.form.get("movie_id")
    movie_title = request.form.get("movie_title")
    current_list = request.form.get("current_list")
    print(f"current list type is: {type(current_list)}, current list value passed to stay is {current_list}") 
    if movie_id and movie_title:
        FAVORITES.add(movie_id)
        flash(f"added {movie_title} to favorites")
    return redirect(url_for('homepage', stay=current_list))


@app.route("/favorites")
def show_favorites():
    if FAVORITES:
        movies = []
        for movie_id in FAVORITES:
            movie_details = tmdb_client.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template("homepage.html", options=OPTIONS, movies=movies)


@app.route("/")
def homepage(stay=None):
    if stay:
        print(True)
        print(f"stay said {stay}")
        value = stay
    else:
        print(False)
        print(f"stay said {stay}")
        value = request.args.get("value", "Popular")
    selected_list = request.args.get("list_type", "popular")

    #reduced name checking for false browser input
    safelock = ["latest", "now_playing", "popular", "top_rated", "upcoming"]
    if any(item == selected_list for item in safelock):
        pass
    else:
        selected_list = "popular"

    movies = tmdb_client.get_movies(how_many=20, list_name=selected_list)
    return render_template(
        "homepage.html", options=OPTIONS, movies=movies, current_list=value
    )


@app.route("/luckyguess")
def lucky():
    value = fake.sentence(nb_words=1)
    movies = tmdb_client.search(value)
    return render_template("lucky.html", options=OPTIONS, movies=movies, value=value)


@app.route("/search")
def search():
    search_query = request.args.get("Sform", "")
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", options=OPTIONS, movies=movies, search_query=search_query)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", options=OPTIONS, movie=details, cast=cast)


@app.route("/today")
def today():
    movies = tmdb_client.get_series_airing()
    today = datetime.date.today()
    return render_template("today.html", options=OPTIONS, movies=movies, today=today)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


if __name__ == "__main__":
    app.run(debug=True)
