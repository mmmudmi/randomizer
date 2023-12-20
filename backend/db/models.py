from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, DateTime
from db.database import Base
from sqlalchemy.orm import relationship

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, unique=False, nullable=False)
    shops = relationship("Shop", back_populates="tag")
    deleted = relationship("Deleted", back_populates="tag")
    
class Shop(Base):
    __tablename__ = "shops"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True, unique=False, nullable=False)
    description = Column(String(300), index=True, unique=False, nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id'))  
    tag = relationship("Tag", back_populates="shops") 
    is_drawn = Column(Boolean, default=False)
    time_drawn = Column(DateTime, default=None, nullable=True)

class Deleted(Base):
    __tablename__ = "deleted"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True, unique=False, nullable=False)
    description = Column(String(300), index=True, unique=False, nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id'))  
    tag = relationship("Tag", back_populates="deleted") 
    is_drawn = Column(Boolean, default=False)
    time_drawn = Column(DateTime, default=None, nullable=True)