CREATE DATABASE blackjack;
CREATE TABLE blackjack.matches(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	user_card VARCHAR(20) NOT NULL,
	house_card VARCHAR(20) NOT NULL,
	round_winner VARCHAR(10) NOT NULL,
	win_card_value VARCHAR(6) NOT NULL
);
