from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
# from fastapi_project import models, crud, schemas  # Updated to absolute import
from fastapi_project import models, crud, schemas
from fastapi_project.database import SessionLocal, engine  # Updated to absolute import

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tags", response_model=List[schemas.Tag])
def read_tags(db: Session = Depends(get_db)):
    tags = crud.get_tags(db)
    return tags

@app.get("/images", response_model=List[schemas.SvgImage])
def read_images(db: Session = Depends(get_db)):
    images = crud.get_images(db)
    return images

@app.get("/images/{tag}", response_model=List[schemas.SvgImage])
def read_images_by_tag(tag: str, db: Session = Depends(get_db)):
    images = crud.get_images_by_tag(db, tag)
    if images is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return images

@app.delete("/images/del", response_model=List[schemas.SvgImage])
def delete_images(image_ids: List[int], db: Session = Depends(get_db)):
    crud.delete_images(db, image_ids)
    return {"message": "Images deleted successfully"}
