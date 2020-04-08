from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from src.database import db

ma = Marshmallow()

class RoomUserModel(db.Model):
  __tablename__ = 'room_user'
  __table_args__ = {'extend_existing': True}
  
  room_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
  deleted_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<RoomUserModel room_id={room_id} user_id={user_id}>'.format(
      room_id=self.room_id,
      user_id=self.item_id,
      count=self.count
    )

class RoomUserSchema(ma.ModelSchema):
  class Meta:
    model = RoomUserModel