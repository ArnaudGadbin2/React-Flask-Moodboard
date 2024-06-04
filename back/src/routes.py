from flask import Blueprint, render_template
from flask import jsonify, request
from models import Element
from extensions import db

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return render_template('index.html')

@api.route("/elements", methods=["GET"])
def element_list():
    elements = Element.query.all()
    return jsonify([{"id": element.id, "type": element.type, "content": element.content} for element in elements])

@api.route("/elements", methods=["POST"])
def element_create():
    body = request.json
    element = Element(
        type=body["type"],
        content=body["content"],
    )
    db.session.add(element)
    db.session.commit()
    return jsonify({"id": element.id, "type": element.type, "content": element.content})

@api.route("/element/<int:id>", methods=["DELETE"])
def element_delete(id):
    element = db.get_or_404(Element, id)
    db.session.delete(element)
    db.session.commit()

    return jsonify({"status": "ok"})