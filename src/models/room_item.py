from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import db

ma = Marshmallow()

class RoomItemModel(db.Model):
  __tablename__ = 'room_item'
  __table_args__ = {'extend_existing': True}
  
  room_id = db.Column(db.Integer, primary_key=True)
  item_id = db.Column(db.Integer, primary_key=True)
  count = db.Column(db.Integer, defaul=0) # そのルームで何回履歴に残ったか(降順におすすめに出すイメージ)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
  deleted_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<RoomItemModel room_id={room_id} item_id={item_id} count={count}>'.format(
      room_id=self.room_id,
      item_id=self.item_id,
      count=self.count
    )

class RoomItemSchema(ma.ModelSchema):
  class Meta:
    model = RoomItemModel