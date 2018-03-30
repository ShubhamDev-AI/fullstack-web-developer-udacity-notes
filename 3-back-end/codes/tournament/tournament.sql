-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

------------------------------------------------------------------------
-- Drop database
------------------------------------------------------------------------
drop database tournament;

------------------------------------------------------------------------
-- Create database and connect to it
------------------------------------------------------------------------
create database tournament;
\c tournament

------------------------------------------------------------------------
-- Create tables
------------------------------------------------------------------------
-- Create 'Player'
create table Player(
	id serial primary key,
	name text not null
);
-- Create 'Match'
create table Match(
	winner integer references Player(id),
	loser integer references Player(id),
	primary key(winner, loser)
);

------------------------------------------------------------------------
-- Insert sample rows into tables
------------------------------------------------------------------------
insert into Player(name) values('A');
insert into Player(name) values('B');
insert into Player(name) values('C');
insert into Player(name) values('D');
insert into Player(name) values('E');
insert into Player(name) values('F');
insert into Player(name) values('G');
insert into Player(name) values('H');
		
insert into Match(winner, loser) values(2, 1);
insert into Match(winner, loser) values(3, 4);
insert into Match(winner, loser) values(6, 5);
insert into Match(winner, loser) values(7, 8);
insert into Match(winner, loser) values(3, 2);
insert into Match(winner, loser) values(6, 7);
insert into Match(winner, loser) values(4, 1);
insert into Match(winner, loser) values(8, 5);
insert into Match(winner, loser) values(3, 6);
insert into Match(winner, loser) values(7, 2);
insert into Match(winner, loser) values(8, 4);
insert into Match(winner, loser) values(5, 1);


------------------------------------------------------------------------
-- Create view to store complex queries
------------------------------------------------------------------------
create view count_winner_view as 
	select winner, count(*) as num
	from Match
	group by(winner);

create view count_loser_view as 
	select loser, count(*) as num
	from Match 
	group by(loser);

create view match_records_view as
	select coalesce(winner, loser) as player, coalesce(w.num, 0) as wins, coalesce(l.num, 0) as loses 
	from count_winner_view as w 
	full outer join count_loser_view as l 
	on (w.winner = l.loser);

create view player_static_view as
	select Player.id, Player.name, coalesce(wins, 0) as wins, coalesce((wins + loses), 0) as matches 
	from match_records_view 
	right join Player on (match_records_view.player = Player.id);





