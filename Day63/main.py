from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title = request.form["book_name"],
            author = request.form["book_author"],
            rating = request.form["book_rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")


@app.route("/edit_rating", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        book_id = request.form['id']
        book = Book.query.get(book_id)
        book.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete_book", methods=["GET"])
def delete_book():
    book_id = request.args.get('id')
    book_to_be_deleted = Book.query.get(book_id)
    db.session.delete(book_to_be_deleted)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
