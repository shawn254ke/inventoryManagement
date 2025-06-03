from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

from .base import Base
from .product_supplier import product_supplier


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2))
    quantity_in_stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates="products")
    suppliers = relationship('Supplier', secondary=product_supplier, back_populates='products')

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"

    @classmethod
    def create(cls, session, name, description, price, quantity_in_stock, category):
        product = cls(
            name=name,
            description=description,
            price=price,
            quantity_in_stock=quantity_in_stock,
            category=category
        )
        session.add(product)
        session.commit()
        return product

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
