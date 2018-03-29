from tournament import *

def test_count_player():
	num_player = countPlayers()
	if num_player != 8:
		raise ValueError("Number of players has to be 8")
	print("{} - Success!".format(test_count_player.__name__))

def test_delete_all_players():
	deletePlayers()
	num_player = countPlayers()
	if num_player != 0:
		raise ValueError("Number of players has to be 0")
	print("{} - Success!".format(test_delete_all_players.__name__))

def test_insert_new_player(name):
	deletePlayers()
	registerPlayer(name)
	num_player = countPlayers()
	if num_player != 1:
		raise ValueError("Number of players has to be 1")
	print("{} - Success!".format(test_insert_new_player.__name__))

def test_get_player_standings():
	records = playerStandings()
	print(records)
	if len(records) != 8:
		raise ValueError("Number of playerStandings has to be 8")
	print("{} - Success!".format(test_get_player_standings.__name__))

def test_delete_all_matches():
	deleteMatches()
	records = playerStandings()
	if len(records) != 0:
		raise ValueError("Number of records has to be 0")
	print("{} - Success!").format(test_delete_all_players.__name__)


if __name__ == '__main__':
	#test_count_player()
	#test_delete_all_players()
	# test_insert_new_player("Jerry")
	# test_get_player_standings()
	test_delete_all_matches()
	# test_delete_all_players()