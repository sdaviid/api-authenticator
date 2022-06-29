from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.types import(
    Date,
    Boolean,
    Time,
    DateTime
)
from sqlalchemy.orm import(
    relationship,
    backref
)
from app.models.base import ModelBase
from app.core.database import Base
from datetime import datetime
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE



class Roles(ModelBase, Base):
    __tablename__ = "roles"
    id = Column(GUID, primary_key=True, index=True, default=GUID_DEFAULT_SQLITE)
    id_user = Column(GUID, allow_null=False)
    value = Column(String(255))
    client_id = Column(String(255))
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, data):
        roles = Roles()
        roles.id_user = data.id_user
        roles.value = data.value
        roles.client_id = data.client_id
        session.add(roles)
        session.commit()
        session.refresh(roles)
        return Roles.find_by_id(session=session, id=roles.id)


    @classmethod
    def check_roles_client_id(cls, session, id_user, client_id):
        return session.query(
            cls.id,
            cls.id_user,
            cls.value,
            cls.client_id,
            cls.date_created
        ).filter(Roles.id_user == id_user, Roles.client_id == client_id).all()
