from sqlalchemy.orm import Query

from src.application.dtos import PaginatedResult, PaginationParameters


def paginate_query(
    query: Query, pagination_params: PaginationParameters
) -> PaginatedResult:
    total = query.count()
    result = query.offset(pagination_params.skip).limit(pagination_params.limit).all()
    return PaginatedResult(result=result, total=total)
