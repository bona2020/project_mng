from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from utils import db

templates=Jinja2Templates(directory='templates')

router = APIRouter(tags=['Tasks'])
#===============================================================================
#                               Tasks Routes
#===============================================================================    
#---------------------------------------------------------------------------------
#1. Get All Tasks
@router.get('/get all taks ')
def root_taks():
    res =db.table('tasks').select('*').execute()
    data = res.data
    return templates.TemplateResponse('home.html',{'request':Request,'tasks':data})
#-------------------------------------------------------------------------------
#2. Create a Task
@router.post('/create task')
def create_task(title: str = Form(...), description: str = Form(...), project_id: int = Form(None)):
    res = db.table('tasks').insert({'title': title, 'description': description, 'project_id': project_id}).execute()
    return {"message": "Task created successfully", "task": res.data}
#-------------------------------------------------------------------------------
#3. Get Task by ID
@router.get('/tasks/{task_id}')
def get_task(task_id: int):      
    res = db.table('tasks').select('*').eq('id', task_id).execute()
    if res.data:
        return {"task": res.data[0]}
    return {"message": "Task not found"}
#-------------------------------------------------------------------------------
#4. Update Task by ID
@router.put('/tasks/{task_id}/update')
def update_task(task_id: int, title: str = Form(...), description: str = Form(...), project_id: int = Form(None)):
    res = db.table('tasks').update({'title': title, 'description': description, 'project_id': project_id}).eq('id', task_id).execute()
    if res.data:
        return {"message": "Task updated successfully", "task": res.data[0]}
    return {"message": "Task not found"}
#-------------------------------------------------------------------------------
#5. Delete Task by ID   
@router.delete('/tasks/{task_id}/delete')
def delete_task(task_id: int):        
    res = db.table('tasks').delete().eq('id', task_id).execute()
    if res.data:
        return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}
#-------------------------------------------------------------------------------
#6. Get Tasks by Project ID
@router.get('/tasks/project/{project_id}')
def get_tasks_by_project(project_id: int):
    res = db.table('tasks').select('*').eq('project_id', project_id).execute()
    return {"tasks": res.data}
#-------------------------------------------------------------------------------
