from interfaces_extractor import config
from interfaces_extractor.services import services
from interfaces_extractor.utils.utils import json_reader, find_key_content
from interfaces_extractor.db import session
from loguru import logger

if __name__ == '__main__':
    json_file = json_reader(config.PATH_TO_FILE)
    native_data = find_key_content(json_file, config.NATIVE_FIELD_KEY)
    native_data = find_key_content(native_data, config.INTERFACE_KEY)

    for key in config.KEYS_TO_DATABASE:
        logger.info(f"Parsing of {key} data started.")
        services.get_interface_subset_and_put_to_database(native_data, key, session)

