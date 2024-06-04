from src.extensions import db
from sqlalchemy.orm import Mapped, mapped_column

class Element(db.Model):
    __tablename__ = 'elements'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    type: Mapped[str]

    def __repr__(self):
        return f'<Element {self.id}>'