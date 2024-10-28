from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

image_tags = Table(
    'image_tags', Base.metadata,
    Column('image_id', Integer, ForeignKey('images.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    images = relationship('SvgImage', secondary=image_tags, back_populates='tags')

class SvgImage(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    width = Column(Integer)
    height = Column(Integer)
    description = Column(String, nullable=True)
    tags = relationship('Tag', secondary=image_tags, back_populates='images')
