from sqlalchemy.orm import Session
from . import models


def get_tags(db: Session):
    return db.query(models.Tag).all()

def get_images(db: Session):
    return db.query(models.SvgImage).all()

def get_images_by_tag(db: Session, tag_name: str):
    return db.query(models.SvgImage).join(models.SvgImage.tags).filter(models.Tag.name == tag_name).all()

def delete_images(db: Session, image_ids: list):
    db.query(models.SvgImage).filter(models.SvgImage.id.in_(image_ids)).delete(synchronize_session=False)
    db.commit()
