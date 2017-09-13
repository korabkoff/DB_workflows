import os
import numpy as np
import time


# get all directories in current one

def get_list_of_dirs(root_folder_path):

    if not root_folder_path:
        return None

    list_of_dir_name = []

    # get all files in subdirectories
    for root, dirs, files in os.walk(root_folder_path):
        list_of_dir_name.extend(dirs)

    return list_of_dir_name


# open files based on provided path to folder
def load_data(file_path):

    if not file_path or not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as file_handler:
        content = file_handler.readlines()
        content = [x.strip() for x in content]
        return content


# get team plaers IDs by team ID
def get_team_ids(teams_players_id, team_id):

    player_ids = (teams_players_id[team_id].split())[1:]
    team_id = (teams_players_id[team_id].split())[1]
    return (team_id, player_ids)


# get team score by summarise players score in team
def get_team_score(team_id):

    team_score = sum(get_player_score(players_score, player_ids))

    return team_ids


# get sorted list of teams by score
def get_sorted_list_of_teams_by_score(teams_filepath, players_scores):

    teams_id_n_score = dict()

    with open(teams_filepath,'r') as teams_data:
        for team in teams_data:

            team = team.split()
            # print('team: ' + str(team))

            team_id = team[0]
            # print('team_id: ' + str(team_id))

            team_players = team[1:]
            # print('team_players: ' + str(team_players))
            team_score = 0
            for player in team_players:

                player_score = players_scores[int(player)]
                # print('player_score: ' + str(player_score))

                team_score += int(player_score)

                teams_id_n_score[int(team_id)] = team_score

            # print('teams_score: '+ str(team_score))
        # print (teams_id_n_score)
    return sorted(teams_id_n_score.items(), key=lambda score: score[1])


# return teams pairwise starting from first
def return_pairwise_id(sorted_by_score):

    sorted_by_score = [id for id, score in (sorted_by_score)]

    matched_teams = list(zip(sorted_by_score[0:len(sorted_by_score):2],
                         sorted_by_score[1:len(sorted_by_score):2]))

    return matched_teams


# make dict of Players scores to efficient serch in it
def make_players_scores_dict(players_filepath):

    if not players_filepath or not os.path.exists(players_filepath):
        return None

    with open(players_filepath, 'r') as players_data:

        players_scores = []

        for player in players_data:
            # print('player: ' + player)
            player_id = player.split()[0]
            # print('player_id: ' + player_id)
            player_score = player.split()[1]
            # print('player_score: ' + player_score)
            players_scores.append(int(player_score))
            # print('players_scores: ' + str(players_scores))
            # print('\n')

        # print('players_scores: ' + str(players_scores[:10]))
    return players_scores
    # return player_id





if __name__ == '__main__':
    start_time = time.time()

    directory = 'test_A'

    players_scores_dict = make_players_scores_dict(directory +'/'+'players.txt')
    print(time.time() - start_time)
    # print('players_scores: ' + str(players_scores_dict[:10]))

    sorted_by_score = get_sorted_list_of_teams_by_score(directory +'/'+'teams.txt', players_scores_dict)
    print(sorted_by_score[:10])
    print(time.time() - start_time)

    matched = return_pairwise_id(sorted_by_score)
    print(matched[:5])
    print(time.time() - start_time)
    filepath = directory +'/'+'pairs.txt'
    with open(filepath, 'w') as output:
        for team_a, team_b in matched:
            output.write(str(team_a) + ' ' + str(team_b) + '\n')

    print(time.time() - start_time)