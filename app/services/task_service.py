from fastapi import HTTPException
# from models import user_task_models
# from schemas import user_task
from sqlalchemy.orm import Session
from app.models.user_task_models import Tasks
from app.schemas import user_task
from sqlalchemy.orm import Session
from datetime import date


def create_task(session: Session, reference_id: str, todolist: str, status:str):
    new_task = Tasks(
        reference_id=reference_id,  # Auth0 user ID
        date=date.today(),
        todolist=todolist,
        status=status  
    )
    session.add(new_task)
    session.commit()
    return new_task


def get_tasks_by_reference_id(db: Session, reference_id: str,skip:int,limit:int):
    tasks= db.query(Tasks).filter(Tasks.reference_id==reference_id).offset(skip).limit(limit).all()
    return tasks
  
def get_id_to_update(session: Session, task_id: int, todolist: str, status: str):
    task = session.query(Tasks).filter(Tasks.task_id == task_id).first()
    # if not task:
    #     return None
    task.todolist = todolist
    task.status = status
    session.commit()
    return task


def get_id_to_delete(session: Session, task_id: int):
    task = session.query(Tasks).filter(Tasks.task_id == task_id).first()

    session.delete(task)
    session.commit()
    return task












# def create_task(db: Session, task_data: user_task.TaskCreate, user_id: int):
#     new_task = Tasks(
#         title=task_data.title,
#         date=task_data.date,
#         status=task_data.status,
#         user_id=user_id
#     )
#     db.add(new_task)
#     db.commit()
#     db.refresh(new_task)
#     return new_task


# def get_tasks(db: Session, user_id: int, skip: int, limit: int):
#     return db.query(Tasks).filter(Tasks.task_user_id == user_id).offset(skip).limit(limit).all()

# def update_task(db: Session, task_id: int, task_data: dict, user_id: int):
#     task = db.query(Tasks).filter(Tasks.task_id == task_id, Tasks.task_user_id == user_id).first()
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     for key, value in task_data.items():
#         setattr(task, key, value)
#     db.commit()
#     db.refresh(task)
#     return task

# def delete_task(db: Session, task_id: int, user_id: int):
#     task = db.query(Tasks).filter(Tasks.task_id == task_id, Tasks.task_user_id == user_id).first()
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     db.delete(task)
#     db.commit()
#     return {"detail": "Task deleted"}



