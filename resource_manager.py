from os import path
from pandas import read_csv
import sys


def get_resource(resource):
    """
    Get the correct path of a ressource, because it's different from local to the final executable
    :param resource: only images for this project, but it can be any file type
    :return: the correct path of the resource depending on if it's local or if it's the final executable
    """
    try:
        base_path = sys._MEIPASS
    except (Exception,):
        base_path = path.abspath(".")
    return path.join(base_path, "./res/") + "/" + resource


def get_config():
    """
    Get the config.csv's path to allow in other scripts to open it and get the user's preferences
    :return: the path of config.csv
    """
    if getattr(sys, "frozen", False):
        executable_path = path.dirname(sys.executable)
    else:
        executable_path = path.dirname(__file__)

    config_path = path.join(executable_path, "config.csv")
    return config_path


dataframe = read_csv(get_config(), delimiter=";", index_col=False)
