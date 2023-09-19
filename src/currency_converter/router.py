from fastapi import APIRouter
from fastapi.responses import JSONResponse
from aiohttp import ClientSession
from src.currency_converter.shemes import Item

router = APIRouter(
    prefix="/api",
    tags=['API'],
)

url = "https://api.coingate.com/v2/rates/merchant/"

@router.get("/rates", response_model=Item)
async def get_currency(from_of: str, to: str, value: int):
    async with ClientSession() as session:
        async with session.get(f"{url}{from_of}/{to}") as response:
            answer = await response.json()
            if not answer:
                return JSONResponse(status_code=400, content={'error': "Bad request"})

            return {"result": answer * value}







