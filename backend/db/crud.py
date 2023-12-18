from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import schemas, models
import random

def get_all(db: Session, model: models.Base):
    return db.query(model).all()

def delete_all(db: Session, model: models.Base):
    db.query(model).delete()
    db.commit()

def get_by_id(db: Session, model: models.Base, id: int):
    return db.query(model).filter(model.id == id).first()

def get_by_name(db: Session, model: models.Base, name: str):
    return db.query(model).filter(model.name == name).first()

def delete_by_id(db: Session, model: models.Base, id: int):
    db.query(model).filter(model.id == id).delete()
    db.commit()

def delete_by_name(db: Session, model: models.Base, name: str):
    db.query(model).filter(model.name == name).delete()
    db.commit()

def create_shop(db: Session, data: schemas.CreateShops):
    for shop in data.shops:
        db_shop = models.Shop(
            name = shop.name,
            description = shop.description,
            tag = get_by_id(db,models.Tag,data.tag_id)
        )
        db.add(db_shop)
        db.commit()
        # db.refresh(db_shop)

def confirm_draw(db: Session, shop_id: int):
    db_shop = db.query(models.Shop).filter(models.Shop.id == shop_id).first()
    db.query(models.Shop).filter(models.Shop.id == shop_id).update({
        "is_drawn": True,
        "time_drawn": func.now(),
    })
    db.commit()
    db.refresh(db_shop)
    return db_shop

def redraw(db: Session, shop_id: int):
    shop = db.query(models.Shop).filter(models.Shop.id == shop_id).first()
    shop.is_drawn = False
    shop.time_drawn = None
    db.commit()

def redraw_all(db: Session, tag_id: int):
    db_shop = db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == True)).all()
    for shop in db_shop:
        shop.is_drawn = False
        shop.time_drawn = None
    db.commit()

def create_tag(db: Session, tag: schemas.Tag):
    db_tag = models.Tag(
        name = tag.name,
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_all_available_by_tag_id(db: Session, tag_id: int):
    return db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == False)).all()

def delete_all_by_tag_id_drawn(db: Session,tag_id: int):
    db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == True)).delete()
    db.commit()

def delete_all_by_tag_id_undrawn(db: Session, tag_id: int):
    db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == False)).delete()
    db.commit()

def draw(db:Session, tag_id: int):
    shops = get_all_available_by_tag_id(db, tag_id)
    return random.choice(shops)

def history_by_tag(db:Session, tag_id: int):
    return db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == True)).all()
