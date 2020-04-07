CREATE TABLE IF NOT EXISTS room_item (
  room_id int(11) unsigned not null comment 'ユーザID',
  item_id int(11) unsigned NOT NULL comment 'アイテムID',
  count int(11) NOT NULL COMMENT '回数',
  created_at datetime not null default current_timestamp comment '登録日時',
  updated_at datetime not null default current_timestamp on update current_timestamp comment '更新日時',
  deleted_at datetime default null comment '削除日時',
  PRIMARY KEY (room_id, item_id),
  FOREIGN KEY(room_id) REFERENCES room(id),
  FOREIGN KEY(item_id) REFERENCES item(id)
);
