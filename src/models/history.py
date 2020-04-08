from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import db

ma = Marshmallow()

class HistoryModel(db.Model):
  __tablename__ = 'history'
  __table_args__ = {'extend_existing': True}
  
  room_id = db.Column(db.Integer, primary_key=True)
  item_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, primary_key=True)
  amount = db.Column(db.Integer, defaul=0)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
  deleted_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<HistoryModel room_id={room_id} user_id={user_id} item_id={item_id} amount={amount}>'.format(
      room_id=self.room_id,
      item_id=self.item_id,
      user_id=self.user_id,
      amount=self.amount
    )

class HistorySchema(ma.ModelSchema):
  class Meta:
    model = HistoryModel