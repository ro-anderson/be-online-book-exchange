import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base


class CategoryTypes(enum.Enum):
    """ Defining Categories Types """

    book = "book"

class Donations(Base):
    """ Donations Entity """

    __tablename__ = "donations"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    category = Column(Enum(CategoryTypes), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Donation: [name={self.name}, category={self.category}, user_id={self.user_id}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.category == other.category
            and self.user_id == other.user_id
        ):
            return True
        return False
