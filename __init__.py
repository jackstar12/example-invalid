from fastapi import APIRouter

invalid_ext: APIRouter = APIRouter(prefix="/invalid", tags=["invalid"])
