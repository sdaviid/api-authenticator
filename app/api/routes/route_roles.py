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

from app.api.rolecheck import RoleChecker


allow_create_resource = RoleChecker(["admin"])

router = APIRouter()


@router.post(
    '/add',
    status_code=status.HTTP_200_OK,
    response_model=RolesDetailData,
    dependencies=[Depends(allow_create_resource)]
)
def add_user(data: RolesAdd, response: Response, db: Session = Depends(get_db)):
    return Roles.add(session=db, data=data)
