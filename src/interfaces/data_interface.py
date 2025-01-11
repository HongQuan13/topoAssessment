from pydantic import BaseModel


class AllDataResponse(BaseModel):
    data: object
