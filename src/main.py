import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routes.main import main_router

logging.basicConfig(level=logging.INFO, force=True)

app = FastAPI()
app.include_router(main_router)


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred"},
    )
