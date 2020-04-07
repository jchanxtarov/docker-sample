CREATE TABLE IF NOT EXISTS history (
  amount int(11) NOT NULL comment '金額',
  room_id int(11) unsigned not null comment 'ルームID',
  item_id int(11) unsigned NOT NULL comment 'アイテムID',
  created_at datetime not null default current_timestamp comment '登録日時',
  updated_at datetime not null default current_timestamp on update current_timestamp comment '更新日時',
  deleted_at datetime default null comment '削除日時',
  PRIMARY KEY (room_id, item_id),
  FOREIGN KEY(room_id) REFERENCES room(id),
  FOREIGN KEY(item_id) REFERENCES item(id)
);
