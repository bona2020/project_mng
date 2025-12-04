from fastapi import APIRouter
from utils import db


router = APIRouter(tags=['Tasks'])
@router.get('/taks')
def root_taks():
    return {"Message":"Hello from Tasks Root"}