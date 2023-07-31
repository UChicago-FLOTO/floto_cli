import configparser
import os

section_name = 'floto'
token_key = 'token'

config = configparser.ConfigParser()


def get_token(config_path=os.path.expanduser('~') + '/.config/floto/floto.ini'):
    # Read the config.ini file
    config.read(config_path)

    # Check if the section and token key exist
    if config.has_section(section_name):
        if config.has_option(section_name, token_key):
            return config.get(section_name, token_key)

    return None


def save_token(token, config_folder='~/.config/floto/', config_file_name='floto.ini'):
    config_folder = os.path.expanduser(config_folder)
    config_path = os.path.join(config_folder, config_file_name)
    print(config_path)
    if not os.path.exists(config_path):
        print("Makedir")
        os.makedirs(config_folder, exist_ok=True)

    if os.path.isfile(config_path):
        config.read(config_path)

    if section_name not in config:
        config.add_section(section_name)

    config[section_name][token_key] = token

    with open(config_path, 'w') as configfile:
        config.write(configfile)
