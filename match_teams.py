import os

# run from directory with tests


def get_sub_directories():

    sub_dirs = []
    for root, dirs, files in os.walk(os.getcwd()):
        sub_dirs.extend(dirs)

    return sub_dirs


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
    if not all_teams_players or not all_players_scores:
        return None

    teams_id_n_score = dict()

    for team_id, team_players in enumerate(all_teams_players):

        # team_score = int()

        teams_id_n_score[team_id] = sum([int(all_players_scores[int(player)])
                                        for player in team_players])

    sorted_teams = [id for id, score in (sorted(teams_id_n_score.items(), key=lambda score: score[1]))]

    return list(zip(sorted_teams[0:len(sorted_teams):2],
                    sorted_teams[1:len(sorted_teams):2]))


def output_matched_teams(pairs_filepath, matched_teams):
    if not matched_teams:
        return None

    with open(pairs_filepath, 'w') as output:
        for team_a, team_b in matched_teams:
            output.write(str(team_a) + ' ' + str(team_b) + '\n')


if __name__ == '__main__':

    for directory in get_sub_directories():
        players_filepath = directory + '/' + 'players.txt'
        teams_filepath = directory + '/' + 'teams.txt'

        out_dir = 'Korabkoff_task_1_team_pairs'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        pairs_filepath = out_dir + '/' + directory + '_pairs.txt'

        output_matched_teams(pairs_filepath, match_teams(load_teams_players(teams_filepath),
                                                         load_players_scores(players_filepath)))

