from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from ..base_class import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cost = Column(String)
    available_quantity = Column(Integer, nullable=False)
    orders = relationship('Order', back_populates='item')
