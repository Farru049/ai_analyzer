from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationUpdate

def create_application(db:Session, user_id:int, data:ApplicationCreate):
    application = Application(
        user_id = user_id,
        company_name = data.company_name,
        role = data.role,
        description = data.description,
        status = data.status,
        notes = data.notes
    )
    db.add(application)
    db.commit()
    db.refresh(application)
    return application

def get_applications(db:Session, user_id:int):
    return db.query(Application).filter(Application.user_id == user_id).all()

def get_application(db:Session, user_id:int, application_id:int):
    application = db.query(Application).filter(Application.user_id == user_id, Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Application not found")
    return application

def update_application(db:Session, user_id:int, application_id: int, data:ApplicationUpdate):
    application = get_application(db, user_id, application_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(application, key, value)
    db.commit()
    db.refresh(application)
    return application


def delete_application(db:Session, user_id: int, application_id: int):
    application = get_application(db, user_id, application_id)
    db.delete(application)
    db.commit()
    return {"detail": "Application deleted successfully"}
