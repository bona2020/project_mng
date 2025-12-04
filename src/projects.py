from fastapi import APIRouter,Request,From
from utils import db
from supabase import client
from fastapi.templating import Jinja2Templates

router=APIRouter(tags=['Projects'])

templates=Jinja2Templates(directory='templates')

@router.get('/projects')
def root_projects(request:Request):
    res = db.table('projects').select('*').execute()
    data = res.data
    return templates.TemplateResponse('home.html', {'request': request, 'tasks': data})
