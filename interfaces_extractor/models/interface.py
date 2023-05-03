from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from interfaces_extractor.db import Base


class Interface(Base):
    __tablename__ = "interface"

    id = Column(Integer, primary_key=True)
    connection = Column(Integer)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    config = Column(JSON)
    type = Column(String(50))
    infra_type = Column(String(50))
    port_channel_id = Column(Integer, ForeignKey('interface.id'))
    children = relationship('Interface', backref='parent', remote_side=[id])
    max_frame_size = Column(Integer)

    def __repr__(self) -> str:
        return f"Name: {self.name}"




