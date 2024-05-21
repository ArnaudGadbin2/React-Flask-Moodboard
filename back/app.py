from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from flask_cors import CORS
import os
from flask import jsonify

load_dotenv()

app = Flask(__name__)
CORS(app)
DATABASE_URL=os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ['SECRET_KEY']


db = SQLAlchemy(app)


class Element(db.Model):
    __tablename__ = 'elements'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    type: Mapped[str]

    def __repr__(self):
        return f'<Element {self.id}>'

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/elements")
def element_list():
    elements = Element.query.all()
    return jsonify([{"id": element.id, "type": element.type, "content": element.content} for element in elements])

@app.route("/elements/create", methods=["POST"])
def element_create():
    body = request.json
    element = Element(
        type=body["type"],
        content=body["content"],
    )
    db.session.add(element)
    db.session.commit()
    return jsonify({"id": element.id, "type": element.type, "content": element.content})

@app.route("/element/<int:id>/delete", methods=["POST"])
def element_delete(id):
    element = db.get_or_404(Element, id)
    db.session.delete(element)
    db.session.commit()

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)