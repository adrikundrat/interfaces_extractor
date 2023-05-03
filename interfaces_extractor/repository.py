from sqlalchemy.orm import sessionmaker

from interfaces_extractor.models.interface import Interface


def put_object_to_db(interface_row: Interface, session: sessionmaker) -> None:
    session.add(interface_row)
    session.commit()
