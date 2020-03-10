
CREATE TABLE GameTable (

game_id INT(5) NOT NULL AUTO_INCREMENT,

game_name VARCHAR(10) NOT NULL,

genre VARCHAR(10) NOT NULL,

release_date INT(12) NOT NULL,

PRIMARY KEY(game_id));

CREATE TABLE MovieTable (

movie_id INT(5) NOT NULL AUTO_INCREMENT,

movie_name VARCHAR(10) NOT NULL,

genre VARCHAR(10) NOT NULL,

release_date INT(10) NOT NULL,

PRIMARY KEY(movie_id));

CREATE TABLE accountTable (

user_id INT(5) NOT NULL AUTO_INCREMENT,

first_name VARCHAR(10) NOT NULL,

last_name VARCHAR(10) NOT NULL,

PRIMARY KEY(user_id)
);

CREATE TABLE MreviewTable (

review_id INT(5) NOT NULL AUTO_INCREMENT,

user_id_1 INT(5) NOT NULL,

movie_id_1 INT(5) NOT NULL,

movie_review VARCHAR(200) NOT NULL,

PRIMARY KEY(review_id),

FOREIGN KEY(movie_id_1) REFERENCES MovieTable(movie_id),

FOREIGN KEY(user_id_1) REFERENCES accountTable(user_id)
);

CREATE TABLE GreviewTable (

review_id INT(5) NOT NULL AUTO_INCREMENT,

user_id_1 INT(5) NOT NULL,

game_id_1 INT(5) NOT NULL,

game_review VARCHAR(200) NOT NULL,

PRIMARY KEY(review_id),

FOREIGN KEY(game_id_1) REFERENCES GameTable(game_id),

FOREIGN KEY(user_id_1) REFERENCES accountTable(user_id)
);