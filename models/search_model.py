import sqlite3
import pandas


def get_genres(conn):
    df = pandas.read_sql('''
        SELECT genre_name, genre_id
        FROM genre
    ''', conn)
    return df


def get_authors(conn):
    df = pandas.read_sql('''
        SELECT author_name, author_id
        FROM author
    ''', conn)
    return df


def get_publishers(conn):
    df = pandas.read_sql('''
        SELECT publisher_name, publisher_id
        FROM publisher
    ''', conn)
    return df


def search_books(conn, df_g, df_p, df_a):
    df = pandas.read_sql('''
        SELECT book.book_id, title, book.genre_id, genre_name, book.publisher_id, publisher_name, year_publication, 
        available_numbers, GROUP_CONCAT(author_name) as 'authors'
        FROM book
        INNER JOIN genre
        ON genre.genre_id = book.genre_id
        INNER JOIN publisher
        ON publisher.publisher_id = book.publisher_id
        INNER JOIN book_author
        ON book_author.book_id = book.book_id
        INNER JOIN author
        ON author.author_id = book_author.author_id
        WHERE book.genre_id IN ({})
        AND book.publisher_id IN ({})
        AND book_author.author_id IN ({})
        GROUP BY book.book_id
    '''. format(df_g, df_p, df_a), conn)
    return df

