from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base

class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer)
    price = Column(DECIMAL(10,2))

    order = relationship('Order', back_populates='items')
    product = relationship('Product')

    def __repr__(self):
        return f"<OrderItem(order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})>"

    @classmethod
    def create(cls, session, order, product, quantity, price):
        item = cls(order=order, product=product, quantity=quantity, price=price)
        session.add(item)
        session.commit()
        return item

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, order_id, product_id):
        return session.query(cls).filter_by(order_id=order_id, product_id=product_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
