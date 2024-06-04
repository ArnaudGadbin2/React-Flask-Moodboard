from flask import Blueprint, render_template
from flask import jsonify, request
from src.models import Element
from src.extensions import db

api = Blueprint('api', __name__)

@api.route('/')
def home():
    return render_template('index.html')

@api.route("/elements", methods=["GET"])
def element_list():
    """Endpoint to get all elements
    ---
    definitions:
      Element:
        type: object
        properties:
          id:
            type: integer
          type:
            type: string
          content:
            type: string
    responses:
      200:
        description: A list of every saved Element
        schema:
          $ref: '#/definitions/Element'
    """
    elements = Element.query.all()
    return jsonify([{"id": element.id, "type": element.type, "content": element.content} for element in elements])

@api.route("/elements", methods=["POST"])
def element_create():
    """Endpoint to create a new element
    ---
    parameters:
      - name: type
        in: path
        type: string
        required: true
        default: text
      - name: content
        in: path
        type: string
        required: true
        default: Bonjour
    definitions:
      Element:
        type: object
        properties:
          id:
            type: integer
          type:
            type: string
          content:
            type: string
    responses:
      200:
        description: The created Element
        schema:
          $ref: '#/definitions/Element'
    """
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
    """Endpoint to delete an element by id
    ---
    responses:
      200:
        description: Ok status
        schema:
          { "status": "ok" }
    """
    element = db.get_or_404(Element, id)
    db.session.delete(element)
    db.session.commit()

    return jsonify({"status": "ok"})