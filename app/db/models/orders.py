from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base_class import Base

class Order(Base):
    id = Column(Integer, primary_key = True, index = True)
    shopping_cart_id = Column(Integer, nullable = False)
    requested_quantity = Column(String, nullable = False)
    total_cost = Column(String, nullable = False)
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship('Item', back_populates = 'orders')