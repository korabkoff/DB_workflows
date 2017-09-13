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


# make dict of Players scores to efficient serch in it
def make_players_scores_dict(players_filepath):

    if not players_filepath or not os.path.exists(players_filepath):
        return None

    with open(players_filepath, 'r') as players_data:

        players_scores = []

        for player in players_data:
            # print('player: ' + player)

            players_scores.append(player.split()[1])
            # print('players_scores: ' + str(players_scores))

        # print('players_scores: ' + str(players_scores[:10]))
    return players_scores

# def make_players_scores_dict(players_filepath):
#
#     with open(players_filepath, 'r') as players_data:
#
#         players_scores = players_data.read()
#
#         for player in players_data:
#             # print('player: ' + player)
#
#             players_scores.append(player.split()[1])
#             # print('players_scores: ' + str(players_scores))
#
#         # print('players_scores: ' + str(players_scores[:10]))
#     return players_scores

# get sorted list of teams by score
def get_sorted_list_of_teams_by_score(teams_filepath, players_scores):

    teams_id_n_score = dict()

    with open(teams_filepath,'r') as teams_data:
        for team in teams_data:
            # team_id, team_players, team_score = int()
            team_id, team_players = team.split()[0], team.split()[1]
            #
            team_score = int()

            for player in team_players:

                player_score = players_scores[int(player)]

                team_score += int(player_score)

            teams_id_n_score[team_id] = team_score

        teams_id_n_score =sorted(teams_id_n_score.items(), key=lambda score: score[1])

        teams_id_n_score = [id for id, score in (teams_id_n_score)]

        teams_id_n_score = list(zip(teams_id_n_score[0:len(teams_id_n_score):2],
                                    teams_id_n_score[1:len(teams_id_n_score):2]))
        return teams_id_n_score


if __name__ == '__main__':
    start_time = time.time()

    directory = 'test_A'

    players_scores_dict = make_players_scores_dict(directory +'/'+'players.txt')
    print(time.time() - start_time)
    # print('players_scores: ' + str(players_scores_dict[:10]))

    pairs = get_sorted_list_of_teams_by_score(directory +'/'+'teams.txt', players_scores_dict)
    # print(pairs[:10])
    print(time.time() - start_time)

    # matched = return_pairwise_id(sorted_by_score)
    # print(matched[:5])

    print(time.time() - start_time)

    filepath = directory +'/'+'pairs.txt'
    with open(filepath, 'w') as output:
        for team_a, team_b in pairs:
            output.write(str(team_a) + ' ' + str(team_b) + '\n')

    print(time.time() - start_time)