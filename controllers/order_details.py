from sqlalchemy.orm import Session
from api import models

def create(db: Session, detail):
    db_detail = models.OrderDetail(
        order_id=detail.order_id,
        sandwich_id=detail.sandwich_id,
        quantity=detail.quantity
    )
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()

def update(db: Session, detail_id: int, detail):
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    update_data = detail.dict(exclude_unset=True)
    db_detail.update(update_data, synchronize_session=False)
    db.commit()
    return db_detail.first()

def delete(db: Session, detail_id: int):
    db_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    db_detail.delete(synchronize_session=False)
    db.commit()
    return {"message": "Order detail deleted"}
