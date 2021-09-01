from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text,
    Table, ForeignKey)
from sqlalchemy.orm import relationship

from .meta import Base

association_table = Table('cart_product', Base.metadata,
                          Column('cart_id', Integer, ForeignKey('cart.id')),
                          Column('product_id', Integer,
                                 ForeignKey('product.id')))


class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    products = relationship('Product', secondary=association_table)

    @property
    def total(self):
        return float(sum([product.value for product in self.products]))


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Float)
