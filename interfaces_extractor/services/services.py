from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from interfaces_extractor import config

from interfaces_extractor.models.interface import Interface
from interfaces_extractor.repository import put_object_to_db
from interfaces_extractor.utils.utils import find_key_content, parse_item
from loguru import logger


def get_interface_subset_and_put_to_database(data: dict, group_name: str, session: Session) -> None:
    """
    Looks for group_name key in data. Loops through its content, calls parser for each elem and puts its output to database.

    :param data:
    :param group_name:
    :param session:
    :return:
    """
    interface_subset = find_key_content(data, group_name)

    for item in interface_subset:
        interface_item = parse_item(item, group_name, session)
        put_object_to_db(interface_item, session)

    logger.info(f"{group_name} data has been successfully added to database.")


def get_first_row_with_name_in_config(session: Session, channel_group_ref: str) -> Interface:
    return session.query(Interface).filter(func.json_extract_path_text(Interface.config, 'name') == channel_group_ref).first()


def get_port_channel_id(item: dict, session: Session) -> Optional[int]:
    """
    Mainly used for non-port channel.
    Looks for channel group config using its key. If present, takes its number parameter that should refer to name
    field of port channel current item refers to. Takes id of the port channel from database and returns it.

    :param item:
    :param session:
    :return:
    """
    channel_group_config = item.get(config.CHANNEL_GROUP_KEY, None)
    if channel_group_config:
        channel_group_ref = str(channel_group_config.get(config.CHANNEL_GROUP_REFERENCE_KEY, ""))
        result = get_first_row_with_name_in_config(session, channel_group_ref)
        return result.id if result else None

    return None
