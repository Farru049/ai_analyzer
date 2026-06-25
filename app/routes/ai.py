from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.application import Application
from app.services.ai_service import analyze_jd
from fastapi import HTTPException, status
router = APIRouter(prefix = "/ai", tags = ["ai"])


@router.post("/analyze/{application_id}")
def analyze_application(application_id:int, db:Session = Depends(get_db),current_user:User = Depends(get_current_user)):
    application = db.query(Application).filter(Application.id == application_id, Application.user_id == current_user.id).first()
    if not application:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Application not found")
    if not application.description:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "JD description is missing")
    analysis = analyze_jd(application.description)
    application.analysis = analysis
    db.commit()
    db.refresh(application)
    return {"analysis": analysis}
    