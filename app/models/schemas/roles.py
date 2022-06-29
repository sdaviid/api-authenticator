from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import baseSchema
from uuid import UUID


class RolesAdd(baseSchema):
    id_user: UUID
    value: str
    client_id: str


class RolesDetailData(baseSchema):
    id: UUID
    id_user: UUID
    value: str
    client_id: str
    date_created: datetime

