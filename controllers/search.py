from app import app
from flask import render_template, request, session
from models.search_model import get_genres, get_authors, get_publishers, search_books
from utils import get_db_connection


@app.route('/search', methods=['get'])
def search():
    conn = get_db_connection()

    df_genres = get_genres(conn)
    df_genres_selected = df_genres['genre_id'].tolist()
    session['genres_selected'] = df_genres_selected
    df_genres_selected = ','.join([str(x) for x in df_genres_selected])

    df_authors = get_authors(conn)
    df_authors_selected = df_authors['author_id'].tolist()
    session['authors_selected'] = df_authors_selected
    df_authors_selected = ','.join([str(x) for x in df_authors_selected])

    df_publishers = get_publishers(conn)
    df_publishers_selected = df_publishers['publisher_id'].tolist()
    session['publishers_selected'] = df_publishers_selected
    df_publishers_selected = ','.join([str(x) for x in df_publishers_selected])

    search_genres = False
    search_publishers = False
    search_authors = False

    if request.values.get("search"):
        if request.values.get("genres"):
            session['genres_selected'] = [int(x) for x in request.values.getlist("genres")]
            df_genres_selected = ','.join(request.values.getlist("genres"))
            search_genres = True
        if request.values.get("publishers"):
            session['publishers_selected'] = [int(x) for x in request.values.getlist("publishers")]
            df_publishers_selected = ','.join(request.values.getlist("publishers"))
            search_publishers = True
        if request.values.get("authors"):
            session['authors_selected'] = [int(x) for x in request.values.getlist("authors")]
            df_authors_selected = ','.join(request.values.getlist("authors"))
            search_authors = True

    df_searched_books = search_books(conn, df_genres_selected, df_publishers_selected, df_authors_selected)

    html = render_template(
        'search.html',
        df_genres=df_genres,
        df_authors=df_authors,
        df_publishers=df_publishers,
        df_searched_books=df_searched_books,
        genres_selected=session['genres_selected'],
        publishers_selected=session['publishers_selected'],
        authors_selected=session['authors_selected'],
        search_genres=search_genres,
        search_publishers=search_publishers,
        search_authors=search_authors,
        len=len
    )
    return html