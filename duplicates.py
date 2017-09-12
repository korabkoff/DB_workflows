import argparse
import sys
import os
from os.path import getsize, join


def parse_args(args):

    def readable_dir(prospective_dir):
        if not os.path.isdir(prospective_dir):
            raise OSError("'{0}' is not a valid path".format(prospective_dir))
        elif os.access(prospective_dir, os.R_OK):
            return prospective_dir
        else:
            raise OSError("'{0}' is not a readable dir".format(prospective_dir))

    parser = argparse.ArgumentParser(description='Show duplicates of files in given folder and subfolders')
    parser.add_argument('filepath', help='File path to folder', type=readable_dir, default=None)
    return parser.parse_args(args)


def get_list_of_files(root_folder_path):
    if not root_folder_path:
        return None

    list_of_dir_name_size = []

    # get all files in subdirectories
    for root, folders, files in os.walk(root_folder_path):
        list_of_dir_name_size.extend(((root, filename, getsize(join(root, filename)))
                            for filename in files))
    return list_of_dir_name_size


def efficiently_get_duplicates(files_list):

    files_list = sorted(files_list, key=lambda file_size: file_size[2], reverse=True)

    dublicates_list = []
    dublicates = 0
    files_list_len = len(files_list)-1
    for index in range(files_list_len):
        if dublicates > 0:
            dublicates -= 1
        else:
            reference_file = files_list[index]
            get_next_file = True

            while get_next_file:
                next_index = index+1+dublicates
                if next_index <= files_list_len:
                    next_file = (files_list[next_index])

                    if reference_file[1:] == next_file[1:]:
                        dublicates_list.append(join(next_file[0], next_file[1]))
                        dublicates += 1
                    else:
                        get_next_file = False
                else:
                    get_next_file = False

    return(dublicates_list)


if __name__ == '__main__':

    try:
        parser = parse_args(sys.argv[1:])
        filepath = parser.filepath
    except OSError as e:
        print(e)
        filepath = None

    if filepath:
        files_list = get_list_of_files(filepath)

        duplicate_list = efficiently_get_duplicates(files_list)

        for duplicate in duplicate_list:
            print(duplicate)

