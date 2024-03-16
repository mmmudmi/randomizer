from fastapi import FastAPI, Response, HTTPException, Depends
from db import database, models, schemas, crud
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import List
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=database.engine)


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
db_session = database.SessionLocal()
#----- CORS --------
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#----- SHOPS --------
@app.post("/api/shops/")
def create_shop(data: schemas.CreateShops, db: Session = Depends(get_db)):
    crud.create_shop(db,data)
    return {
        "message": "เพิ่มร้านค้าสำเร็จ!",
    }

@app.post("/api/shops/group/")
def create_shop_group(data: schemas.CreateShops, db: Session = Depends(get_db)):
    crud.create_shop_group(db,data)

@app.get("/api/shops/}", response_model=List[schemas.Shop])
def read_shops(db: Session = Depends(get_db)):
    return crud.get_all(db,models.Shop)

@app.get("/api/shops/tag/{tag_id}", response_model=List[schemas.Shop])
def read_shops_by_tag(tag_id: int, db: Session = Depends(get_db)):
    return crud.get_all_available_by_tag_id(db,tag_id)

@app.get("/api/shops/{shop_id}", response_model=schemas.ShopDetails)
def read_shop(shop_id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.Shop, shop_id)

@app.delete("/api/shops/{shop_id}")
def delete_shop(shop_id: int, db: Session = Depends(get_db)):
    crud.delete_by_shopId(db, shop_id)
    return {
        "message": "ลบสำเร็จ!"
    }

@app.delete("/api/reset/")
def delete_all( db: Session = Depends(get_db)):
    crud.delete_all(db, models.Shop)
    crud.delete_all(db, models.Deleted)
    return {
        "message": "ลบร้านค้าทั้งหมดสำเร็จ!"
    }

@app.delete("/api/shops/drawn/tag/{tag_id}")
def delete_shops_drawn(tag_id: int, db: Session = Depends(get_db)):
    crud.delete_all_by_tag_id_drawn(db, tag_id)
    return {
        "message": "ลบร้านค้าทั้งหมดสำเร็จ!"
    }

@app.delete("/api/shops/undrawn/tag/{tag_id}")
def delete_shops_undrawn(tag_id: int, db: Session = Depends(get_db)):
    crud.delete_all_by_tag_id_undrawn(db, tag_id)
    return {
        "message": "ลบร้านค้าทั้งหมดสำเร็จ!"
    }

@app.put("/api/shops/confirm/draw/{shop_id}", response_model=schemas.ShopDetails)
def confirm_draw(shop_id: int, db: Session = Depends(get_db)):
    return crud.confirm_draw(db, shop_id)

@app.get("/api/shops/draw/tag/{tag_id}", response_model=schemas.Shop)
def draw(tag_id: int, db: Session = Depends(get_db)):
    return crud.draw(db, tag_id)

@app.put("/api/shops/redraw/{shop_id}")
def redraw(shop_id: int, db: Session = Depends(get_db)): 
    crud.redraw(db, shop_id)
    return {
        "message": "เรียกจับใหม่สำเร็จ!"
    }

@app.put("/api/shops/redraw/tag/{tag_id}")
def redraw_all(tag_id: int, db: Session = Depends(get_db)): 
    crud.redraw_all(db, tag_id)
    return {
        "message": "เรียกจับใหม่ทั้งหมดสำเร็จ!"
    }

@app.get("/api/history/tag/{tag_id}", response_model=List[schemas.ShopDetails])
def history_by_tag(tag_id: int, db: Session = Depends(get_db)):
    return crud.history_by_tag(db, tag_id)

#----- TAGS --------
@app.post("/api/tag/{tag_name}")
def create_tag(tag_name: str, db: Session = Depends(get_db)):
    return crud.create_tag(db, tag_name)

@app.get("/api/tags/", response_model=List[schemas.Tag])
def get_tags(db: Session = Depends(get_db)):
    return crud.get_all(db,models.Tag)

@app.get("/api/tagsInfo/", response_model=List[schemas.TagInfo])
def get_tags_info(db: Session = Depends(get_db)):
    return crud.get_tags_info(db)

@app.delete("/api/tags/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    crud.delete_by_id(db, models.Tag, tag_id)
    return {
        "message": "ลบสำเร็จ!"
    }

#----- DELETED --------
@app.delete("/api/deleted/tag/{tag_id}")
def empty_deleted(tag_id: int,db: Session = Depends(get_db)):
    crud.empty_deleted_byTag(db,tag_id)

@app.get("/api/deleted/tag/{tag_id}",response_model=List[schemas.ShopDetails])
def all_deleted_shops(tag_id: int,db: Session = Depends(get_db)):
    return crud.get_all_deleted_byTag(db,tag_id)

@app.put("/api/deleted/redraw/{shop_id}")
def redraw_deleted_shops(shop_id: int,db: Session = Depends(get_db)):
    return crud.deleted_to_shop(db,shop_id)
