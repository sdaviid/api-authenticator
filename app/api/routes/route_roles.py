from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter
)

from app.api.deps import(
    get_current_active_user
)

from app.models.domain.roles import(
    Roles
)

from app.models.schemas.roles import(
	RolesDetailData,
	RolesAdd
)

from app.core.database import get_db


router = APIRouter()


@router.post(
    '/add',
    status_code=status.HTTP_200_OK,
    response_model=RolesDetailData
)
def add_user(data: RolesAdd, response: Response, db: Session = Depends(get_db)):
    return Roles.add(session=db, data=data)
