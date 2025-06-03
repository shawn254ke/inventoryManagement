from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey

from sqlalchemy.orm import relationship
from .base import Base
from .order_item import OrderItem
import datetime

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(50))
    total_amount = Column(DECIMAL(10,2))

    customer = relationship('Customer', back_populates='orders')
    items = relationship('OrderItem', back_populates='order', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Order(id={self.id}, customer_id={self.customer_id}, total_amount={self.total_amount})>"

    @classmethod
    def create(cls, session, customer, status, total_amount):
        order = cls(customer=customer, status=status, total_amount=total_amount)
        session.add(order)
        session.commit()
        return order

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
