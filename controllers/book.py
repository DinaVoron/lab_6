from app import app
from flask import render_template, request, session


@app.route('/book', methods=['get'])
def book():
    html = render_template(
        'book.html'
    )
    return html
