from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db
import uuid

ma = Marshmallow()

class RoomModel(db.Model):
  __tablename__ = 'room'
  __table_args__ = {'extend_existing': True}
  
  # id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def __repr__(self):
    return '<RoomModel id={id} name={name}>'.format(
      id=self.id,
      name=self.name
    )

class RoomSchema(ma.ModelSchema):
  class Meta:
    model = RoomModel