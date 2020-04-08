CREATE TABLE IF NOT EXISTS room_user (
  room_id int(11) unsigned not null comment 'ルームID',
  user_id int(11) unsigned not null comment 'ユーザID',
  created_at datetime not null default current_timestamp comment '登録日時',
  updated_at datetime not null default current_timestamp on update current_timestamp comment '更新日時',
  deleted_at datetime default null comment '削除日時',
  PRIMARY KEY (room_id, user_id),
  FOREIGN KEY(room_id) REFERENCES room(id),
  FOREIGN KEY(user_id) REFERENCES user(id)
);
