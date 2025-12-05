from fastapi import APIRouter, Request, Form

from utils import db
from supabase import client
from fastapi.templating import Jinja2Templates

router=APIRouter(tags=['Projects'])

templates=Jinja2Templates(directory='templates')

#===============================================================================
#                               Projects Routes
#===============================================================================
#---------------------------------------------------------------------------------
#1. Get All Projects
@router.get('/projects/all')
def get_all_projects():
    res = db.table('projects').select('*').execute()
    data = res.data
    return {"projects": data}   
#-------------------------------------------------------------------------------
#2. create a Project
@router.post('/projects/create')
def create_project(name: str = Form(...), description: str = Form(...),budget: int = Form(...),duration: int = Form(...)):
    res = db.table('projects').insert({'name': name, 'description': description},).execute()
    return {"message": "Project created successfully", "project": res.data}

#-------------------------------------------------------------------------------
#3. Get Project by ID
@router.get('/projects/{project_id}')
def get_project(project_id: int):
    res = db.table('projects').select('*').eq('id', project_id).execute()
    if res.data:
        return {"project": res.data[0]}
    return {"message": "Project not found"}
#-------------------------------------------------------------------------------
#4. Update Project by ID    
@router.put('/projects/{project_id}/update')
def update_project(project_id: int, name: str = Form(...), description: str = Form(...)):
    res = db.table('projects').update({'name': name, 'description': description}).eq('id', project_id).execute()
    if res.data:
        return {"message": "Project updated successfully", "project": res.data[0]}
    return {"message": "Project not found"} 
#-------------------------------------------------------------------------------
#5. Delete Project by ID        
@router.delete('/projects/{project_id}/delete')
def delete_project(project_id: int):        
    res = db.table('projects').delete().eq('id', project_id).execute()
    if res.data:
        return {"message": "Project deleted successfully"}
    return {"message": "Project not found"} 
#-------------------------------------------------------------------------------
#6. Get Projects with their Tasks
@router.get('/projects/with-tasks')     
def get_projects_with_tasks():
    res = db.table('projects').select('*, tasks(*)').execute()
    return {"projects_with_tasks": res.data}    
#-------------------------------------------------------------------------------
#7. Get Tasks for a Specific Project
@router.get('/projects/{project_id}/tasks')     
def get_tasks_for_project(project_id: int):
    res = db.table('tasks').select('*').eq('project_id', project_id).execute()
    return {"tasks": res.data}  
#-------------------------------------------------------------------------------
#8. Assign Task to Project
@router.post('/projects/{project_id}/assign-task')
def assign_task_to_project(project_id: int, task_id: int = Form(...)):
    res = db.table('tasks').update({'project_id': project_id}).eq('id', task_id).execute()
    if res.data:
        return {"message": "Task assigned to project successfully", "task": res.data[0]}
    return {"message": "Task not found"}
#-------------------------------------------------------------------------------


