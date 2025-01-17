#!/usr/bin/env python3

#
#  Project Zomboid Dedicated Server using SteamCMD Docker Image.
#  Copyright (C) 2021-2022 Renegade-Master [renegade.master.dev@protonmail.com]
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""
Author: Renegade-Master
Description:
    Script for editing the Project Zomboid Dedicated Server
    configuration file
"""

import argparse
import sys
from configparser import RawConfigParser


def save_config(config_parser: RawConfigParser, config_file_path: str) -> None:
    """
    Saves the server config file
    :param config_parser: Dictionary of the values
    :param config_file_path: Path to the server config file
    :return: None
    """

    # Overwrite the file value with the new value
    with open(config_file_path, "w", encoding="utf-8") as file:
        config_parser.write(file, space_around_delimiters=False)


def load_config(config_file_path: str) -> RawConfigParser:
    """
    Loads the server config file
    :param config_file_path: Path to the server config file
    :return: ConfigParser Object containing the values
    """

    # Ensure that the file starts with a Section
    with open(config_file_path, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        if lines[0] != "[ServerConfig]\n":
            file.seek(0)
            file.write("[ServerConfig]\n")
            for line in lines:
                file.write(line)

    config_parser: RawConfigParser = RawConfigParser()
    config_parser.optionxform = lambda option: option

    if config_parser.read(config_file_path) is not None:
        return config_parser
    raise TypeError("Config file is invalid!")


def check_server_config_file(config_file_path: str) -> bool:
    """
    Checks if the server config file exists
    :param config_file_path: Path to the server config file
    :return: True if the file exists, False if not
    """

    try:
        with open(config_file_path, "r", encoding="utf-8") as _:
            return True
    except FileNotFoundError:
        sys.stderr.write(f"{config_file_path} not found!\n")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Edits Project Zomboid Dedicated Server config file"
    )
    parser.add_argument("config_file", help="Path to the server config file")
    parser.add_argument("key", help="Key to edit or retrieve")
    parser.add_argument("value", nargs="?", help="New value to assign to key")

    args = parser.parse_args()

    config_file: str = args.config_file
    key: str = args.key

    if check_server_config_file(config_file):
        config: RawConfigParser = load_config(config_file)

        if args.value is None:
            # Return the value of the given key
            if "ServerConfig" in config:
                if key in config["ServerConfig"]:
                    print(f"{config['ServerConfig'][key]}")
        else:
            # Assign a new value
            value: str = args.value

            # Set the desired value
            config["ServerConfig"][key] = value

            # Save the config file
            save_config(config, config_file)
