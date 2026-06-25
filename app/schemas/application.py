from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ApplicationCreate(BaseModel):
    company_name:str
    role:str
    status: str = 'pending'
    description: Optional[str] = None
    notes: Optional[str] = None

class ApplicationUpdate(BaseModel):
    company_name: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    id:int
    company_name:str
    role:str
    status:str
    description: Optional[str] = None
    notes: Optional[str] = None
    applied_at: datetime
    
    class Config:
        from_attributes = True