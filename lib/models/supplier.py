
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base
from .product_supplier import product_supplier

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_person = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)

    products = relationship('Product', secondary='product_supplier', back_populates='suppliers')

    def __repr__(self):
        return f"<Supplier(id={self.id}, name='{self.name}')>"

    @classmethod
    def create(cls, session, name, contact_person, phone, email, address):
        supplier = cls(name=name, contact_person=contact_person, phone=phone, email=email, address=address)
        session.add(supplier)
        session.commit()
        return supplier

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
