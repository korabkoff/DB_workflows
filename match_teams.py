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

def load_players_scores(file_path):
    if not file_path or not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as players_data:
        return [player.split()[1] for player in players_data]


def load_teams_players(file_path):
    if not file_path or not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as players_data:
        return [player.split()[1:] for player in players_data]


def match_teams(all_teams_players, all_players_scores):

    teams_id_n_score = dict()

    for team_id, team_players in enumerate(all_teams_players):

        team_score = int()

        teams_id_n_score[team_id] = sum([int(all_players_scores[int(player)])
                                                    for player in team_players])

    sorted_teams = [id for id, score in (sorted(teams_id_n_score.items(), key=lambda score: score[1]))]

    return list(zip(sorted_teams[0:len(sorted_teams):2],
                             sorted_teams[1:len(sorted_teams):2]))


if __name__ == '__main__':
    start_time = time.time()

    directory = 'test_A'
    players_filepath = directory +'/'+'players.txt'
    teams_filepath = directory +'/'+'teams.txt'

    pairs = match_teams(load_teams_players(teams_filepath), load_players_scores(players_filepath))

    # players_scores_dict = make_players_scores_dict(directory +'/'+'players.txt')
    print(time.time() - start_time)
    print('pairs: ' + str(pairs[:10]))

    filepath = directory +'/'+'pairs.txt'
    with open(filepath, 'w') as output:
        for team_a, team_b in pairs:
            output.write(str(team_a) + ' ' + str(team_b) + '\n')

    print(time.time() - start_time)