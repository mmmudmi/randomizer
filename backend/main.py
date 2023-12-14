from fastapi import FastAPI, Response, HTTPException, Depends
from db import database, models, schemas, crud
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import List

app = FastAPI()
db_session = database.SessionLocal()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#----- SHOPS --------
@app.post("/shops/", response_model=schemas.Shop)
def create_shop(shop: schemas.Shop, db: Session = Depends(get_db)):
    return crud.create_shop(db, shop)

@app.get("/shops/}", response_model=List[schemas.Shop])
def read_shops(db: Session = Depends(get_db)):
    return crud.get_all(db,models.Shop)

@app.get("/shops/tag/{tag_id}", response_model=List[schemas.Shop])
def read_shops_by_tag(tag_id: int, db: Session = Depends(get_db)):
    return crud.get_all_available_by_tag_id(db,tag_id)

@app.get("/shops/{shop_id}", response_model=schemas.ShopDetails)
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.Shop, shop_id)

@app.delete("/shops/{shop_id}")
def delete_shop(shop_id: int, db: Session = Depends(get_db)):
    crud.delete_by_id(db, models.Shop, shop_id)
    return {
        "message": "ลบสำเร็จ!"
    }

@app.delete("/shops/")
def delete_shops( db: Session = Depends(get_db)):
    crud.delete_all(db, models.Shop)
    return {
        "message": "ลบร้านค้าทั้งหมดสำเร็จ!"
    }

@app.delete("/shops/drawn/tag/{tag_id}")
def delete_shops_drawn(tag_id: int, db: Session = Depends(get_db)):
    crud.delete_all_by_tag_id_drawn(db, tag_id)
    return {
        "message": "ลบร้านค้าทั้งหมดสำเร็จ!"
    }

@app.delete("/shops/undrawn/tag/{tag_id}")
def delete_shops_undrawn(tag_id: int, db: Session = Depends(get_db)):
    crud.delete_all_by_tag_id_undrawn(db, tag_id)
    return {
        "message": "ลบร้านค้าทั้งหมดสำเร็จ!"
    }

@app.put("/shops/confirm/draw/{shop_id}", response_model=schemas.ShopDetails)
def confirm_draw(shop_id: int, db: Session = Depends(get_db)):
    return crud.confirm_draw(db, shop_id)

@app.get("/shops/draw/tag/{tag_id}", response_model=schemas.Shop)
def draw(tag_id: int, db: Session = Depends(get_db)):
    return crud.draw(db, tag_id)

@app.put("/shops/redraw/{shop_id}")
def redraw(shop_id: int, db: Session = Depends(get_db)): 
    crud.redraw(db, shop_id)
    return {
        "message": "เรียกจับใหม่สำเร็จ!"
    }

@app.put("/shops/redraw/tag/{tag_id}")
def redraw_all(tag_id: int, db: Session = Depends(get_db)): 
    crud.redraw_all(db, tag_id)
    return {
        "message": "เรียกจับใหม่ทั้งหมดสำเร็จ!"
    }

#----- TAGS --------
@app.post("/tags/", response_model=schemas.Tag)
def create_tag(tag: schemas.Tag, db: Session = Depends(get_db)):
    return crud.create_tag(db, tag)

@app.get("/tags/", response_model=List[schemas.Shop])
def delete_tags(db: Session = Depends(get_db)):
    return crud.get_all(db,models.Tag)

@app.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    crud.delete_by_id(db, models.Tag, tag_id)
    return {
        "message": "ลบสำเร็จ!"
    }
