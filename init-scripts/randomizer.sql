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
    shop_count int,
    foreign key(tag_id) references tags (id) ON DELETE CASCADE
);

CREATE TABLE deleted (
    id int auto_increment primary key,
    name varchar(200) not null,
    description varchar(300) not null,
    tag_id int,
    is_drawn boolean,
    time_drawn DateTime,
    shop_count int,
    foreign key(tag_id) references tags (id) ON DELETE CASCADE
);

INSERT INTO tags (name) VALUES ('Food');

INSERT INTO tags (name) VALUES ('Beverages');

INSERT INTO tags (name) VALUES ('Gift Shop');

INSERT INTO tags (name) VALUES ('Food Truck');

INSERT INTO tags (name) VALUES ('Others');