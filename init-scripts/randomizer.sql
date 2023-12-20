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
    is_drawn boolean,
    time_drawn DateTime,
    foreign key(tag_id) references tags (id)
);

CREATE TABLE deleted (
    id int auto_increment primary key,
    name varchar(200) not null,
    description varchar(300) not null,
    tag_id int,
    is_drawn boolean,
    time_drawn DateTime,
    foreign key(tag_id) references tags (id)
);

INSERT INTO tags (name) VALUES ('อาหาร');

INSERT INTO tags (name) VALUES ('เครื่องดื่ม');

INSERT INTO tags (name) VALUES ('กิ๊ฟช็อป');

INSERT INTO tags (name) VALUES ('foodtruck');

INSERT INTO tags (name) VALUES ('อื่นๆ');