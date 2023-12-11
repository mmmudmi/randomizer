CREATE DATABASE IF NOT EXISTS randomizer;

CREATE USER 'admin' @'%' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON randomizer.* TO 'admin' @'%';

FLUSH PRIVILEGES;

USE randomizer;

CREATE TABLE tags (
    id int auto_increment primary key,
    name varchar(100) not null
);

CREATE TABLE shops (
    id int auto_increment primary key,
    name varchar(200) not null,
    description varchar(300) not null,
    tag_id int,
    foreign key(tag_id) references tags (id)
);

CREATE TABLE history (
    id int auto_increment primary key,
    name varchar(200) not null,
    description varchar(300) not null,
    tag_id int,
    time datetime not null,
    foreign key(tag_id) references tags (id)
);

INSERT INTO tags (name) VALUES ('เครื่องดื่ม');

INSERT INTO tags (name) VALUES ('อาหาร');

INSERT INTO tags (name) VALUES ('กิ๊ฟช็อป');