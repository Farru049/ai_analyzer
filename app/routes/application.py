from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.user import User
from app.dependencies import get_db, get_current_user
from app.schemas.application import ApplicationResponse, ApplicationCreate, ApplicationUpdate
from app.services.application_service import create_application, get_applications, get_application, update_application, delete_application

router = APIRouter(prefix = "/applications", tags = ["applications"])

@router.post("/", response_model = ApplicationResponse)
def create(data:ApplicationCreate, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return create_application(db, current_user.id, data)

@router.get("/", response_model = List[ApplicationResponse])
def get_all(db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return get_applications(db, current_user.id)

@router.get("/{application_id}",response_model = ApplicationResponse)
def get_one(application_id:int, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return get_application(db, current_user.id, application_id)

@router.put("/{application_id}", response_model = ApplicationResponse)
def update(application_id:int, data:ApplicationUpdate, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return update_application(db, current_user.id, application_id, data)

@router.delete("/{application_id}")
def delete(application_id:int, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return delete_application(db, current_user.id, application_id)