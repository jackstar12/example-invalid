from fastapi import APIRouter

from lnbits.db import Database

db = Database("ext_example")

example_ext: APIRouter = APIRouter(prefix="/example", tags=["example"])
