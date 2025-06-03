from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)

    orders = relationship('Order', back_populates='customer', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}')>"

    @classmethod
    def create(cls, session, name, phone, email, address):
        customer = cls(name=name, phone=phone, email=email, address=address)
        session.add(customer)
        session.commit()
        return customer

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
