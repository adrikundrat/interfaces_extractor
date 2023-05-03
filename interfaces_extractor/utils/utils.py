import json
from typing import Optional

from sqlalchemy.orm import Session

from interfaces_extractor.models.interface import Interface


def find_key_content(dictionary: dict, child_key: str) -> Optional[dict]:
    """
    Method to recursively look for exact child_key in dict and return its content

    :param dictionary:
    :param child_key:
    :return:
    """

    if child_key in dictionary:
        return dictionary[child_key]

    for value in dictionary.values():
        if isinstance(value, dict):
            result = find_key_content(value, child_key)
            if result is not None:
                return result

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result = find_key_content(item, child_key)
                    if result is not None:
                        return result


def json_reader(filename: str) -> json:
    with open(filename) as f:
        return json.load(f)


def create_full_name(group_name: str, item: dict) -> str:
    """
    Generates name that will be added to database col name.

    :param group_name:
    :param item:
    :return:
    """
    return f"{group_name}{str(item.get('name', ''))}"


def parse_item(item: dict, group_name: str, session: Session) -> Interface:
    """
    Used for parsing items in interface group. Processes its content to be able to store in database and returns
    Interface typed element.

    :param item:
    :param group_name:
    :param session:
    :return:
    """
    from interfaces_extractor.services.services import get_port_channel_id

    interface_name = create_full_name(group_name, item)
    description = item.get("description", None)
    max_frame_size = item.get("mtu", None)
    port_channel_id = get_port_channel_id(item, session)

    return Interface(
        name=interface_name,
        description=description,
        max_frame_size=max_frame_size,
        config=item,
        port_channel_id=port_channel_id,
    )
