from sqlalchemy import Column, Integer, ForeignKey, Table
from .base import Base

from sqlalchemy.orm import relationship

product_supplier = Table(
    'product_supplier', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('supplier_id', Integer, ForeignKey('suppliers.id'), primary_key=True)
)
