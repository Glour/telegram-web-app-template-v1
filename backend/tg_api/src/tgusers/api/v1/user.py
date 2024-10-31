from fastapi import APIRouter, Depends

from infrastructure.api_services.common.exceptions import generic_exception_handler
from infrastructure.database.repo.requests import RequestsRepo, get_database_repo

router = APIRouter()


@router.get(
    "/{user_id}",
)
async def user_info(
        user_id: int,
        repo: RequestsRepo = Depends(get_database_repo),
):
    return await generic_exception_handler(
        async_func=repo.users.get,
        args=(user_id,)
    )


@router.patch(
    "/{user_id}",
)
async def update_user(
        user_id: int,
        data: dict,
        repo: RequestsRepo = Depends(get_database_repo),
):
    return await generic_exception_handler(
        async_func=repo.users.update,
        args=(user_id,),
        kwargs=data
    )