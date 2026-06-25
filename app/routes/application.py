from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import List
from app.models.user import User
from app.dependencies import get_db, get_current_user
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.schemas.application import ApplicationResponse, ApplicationCreate, ApplicationUpdate
from app.services.application_service import create_application, get_applications, get_application, update_application, delete_application

limiter = Limiter(key_func=get_remote_address)
router = APIRouter(prefix = "/applications", tags = ["applications"])

@router.post("/", response_model = ApplicationResponse)
@limiter.limit("5/minute")
def create(request: Request,data:ApplicationCreate, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    # ratelimiting
    # Implement rate limiting logic here
    
    return create_application(db, current_user.id, data)

@router.get("/", response_model = List[ApplicationResponse])
@limiter.limit("30/minute")
def get_all(request:Request,db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return get_applications(db, current_user.id)

@router.get("/{application_id}",response_model = ApplicationResponse)
@limiter.limit("30/minute")
def get_one(request:Request,application_id:int, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return get_application(db, current_user.id, application_id)

@router.put("/{application_id}", response_model = ApplicationResponse)
@limiter.limit("10/minute")
def update(request:Request,application_id:int, data:ApplicationUpdate, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return update_application(db, current_user.id, application_id, data)

@router.delete("/{application_id}")
@limiter.limit("10/minute")
def delete(request:Request,application_id:int, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return delete_application(db, current_user.id, application_id)