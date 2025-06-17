from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Book mapping
BOOKS = {
    f'k{i}': f'Book {i}' for i in range(1, 13)
}

@app.route('/')
def index():
    return render_template('index.html', books=BOOKS)

@app.route('/book/<book_id>')
def show_book(book_id):
    if book_id not in BOOKS:
        abort(404)
    try:
        with open(os.path.join('books', f'{book_id}.html'), encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        abort(404)
    return render_template('book.html', books=BOOKS, book_title=BOOKS[book_id], book_content=content)

if __name__ == '__main__':
    app.run(debug=True)
