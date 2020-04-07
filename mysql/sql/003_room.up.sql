CREATE TABLE IF NOT EXISTS room (
  id INT(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  name VARCHAR(255) NOT NULL comment 'ルーム名',
  created_at datetime not null default current_timestamp comment '登録日時',
  updated_at datetime not null default current_timestamp on update current_timestamp comment '更新日時',
  deleted_at datetime default null comment '削除日時',
  PRIMARY KEY(id)
);
