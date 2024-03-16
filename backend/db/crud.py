from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import schemas, models
import random
from typing import List


def get_all(db: Session, model: models.Base):
    return db.query(model).all()

def get_tags_info(db: Session):
    all_tags = db.query(models.Tag).all()
    list_tag_info = []
    for tag in all_tags:
        tag_info = schemas.TagInfo(
            id=tag.id,
            name=tag.name,
            count=len(tag.shops)
        )
        list_tag_info.append(tag_info)
    return list_tag_info

def get_by_id(db: Session, model: models.Base, id: int):
    return db.query(model).filter(model.id == id).first()

def get_by_name(db: Session, model: models.Base, name: str):
    return db.query(model).filter(model.name == name).first()

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

def create_shop_group(db: Session, data: schemas.CreateShops):
    names = ""
    descriptions = ""
    for index, shop in enumerate(data.shops):
        names += shop.name
        descriptions += shop.description
        if index < len(data.shops) - 1:
            names += "\n"
            descriptions += "\n"
    db_shop = models.Shop (
        name = names,
        description = descriptions,
        tag = get_by_id(db,models.Tag,data.tag_id),
        shop_count = len(data.shops),
    )
    db.add(db_shop)
    db.commit()

def confirm_draw(db: Session, shop_id: int):
    db_shop = db.query(models.Shop).filter(models.Shop.id == shop_id).first()
    db.query(models.Shop).filter(models.Shop.id == shop_id).update({
        "is_drawn": True,
        "time_drawn": func.convert_tz(func.now(), 'UTC', 'Asia/Bangkok')
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

def create_tag(db: Session, tag_name: str):
    db_tag = models.Tag(
        name = tag_name,
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_all_available_by_tag_id(db: Session, tag_id: int):
    return db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == False)).all()

def draw(db:Session, tag_id: int):
    shops = get_all_available_by_tag_id(db, tag_id)
    return random.choice(shops)

def history_by_tag(db:Session, tag_id: int):
    return db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == True)).all()

# delete

def shop_to_deleted(db: Session, shop_id: int):
    shop_to_move = db.query(models.Shop).filter(models.Shop.id == shop_id).first()
    if shop_to_move:
        deleted_shop = models.Deleted(
            name=shop_to_move.name,
            description=shop_to_move.description,
            tag_id=shop_to_move.tag_id,
            is_drawn=shop_to_move.is_drawn,
            time_drawn=func.convert_tz(func.now(), 'UTC', 'Asia/Bangkok'),
            shop_count= shop_to_move.shop_count,
        )

        db.add(deleted_shop)
        db.delete(shop_to_move)
        db.commit()
        db.refresh(deleted_shop)

def deleted_to_shop(db: Session, shop_id: int):
    shop_to_move = db.query(models.Deleted).filter(models.Deleted.id == shop_id).first()
    if shop_to_move:
        shop = models.Shop(
            name=shop_to_move.name,
            description=shop_to_move.description,
            tag_id=shop_to_move.tag_id,
            is_drawn=shop_to_move.is_drawn,
            time_drawn=func.convert_tz(func.now(), 'UTC', 'Asia/Bangkok'),
            shop_count= shop_to_move.shop_count,
        )
        db.add(shop)
        db.delete(shop_to_move)
        db.commit()
        db.refresh(shop)

def delete_all(db: Session, model: models.Base):
    db.query(model).delete()
    db.commit()

def delete_by_id(db: Session, model: models.Base, id: int):
    db.query(model).filter(model.id == id).delete()
    db.commit()

def delete_by_shopId(db: Session, id: int):
    shop_to_deleted(db,id)

def delete_all_by_tag_id_drawn(db: Session,tag_id: int):
    shops = db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == True))
    for shop in shops:
        shop_to_deleted(db,shop.id)

def delete_all_by_tag_id_undrawn(db: Session, tag_id: int):
    shops = db.query(models.Shop).filter((models.Shop.tag_id == tag_id) & (models.Shop.is_drawn == False))
    for shop in shops:
        shop_to_deleted(db,shop.id)

def empty_deleted_byTag(db: Session,tag_id: int):
    db.query(models.Deleted).filter(models.Deleted.tag_id==tag_id).delete()
    db.commit()

def get_all_deleted_byTag(db: Session, tag_id: int):
    return db.query(models.Deleted).filter(models.Deleted.tag_id == tag_id).all()
