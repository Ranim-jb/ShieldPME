
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default="analyst")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    asset_type = Column(String(100), nullable=False)
    ip_address = Column(String(45))
    operating_system = Column(String(100))
    criticality = Column(String(50), default="medium")
    status = Column(String(50), default="active")
    created_at = Column(DateTime, default=datetime.utcnow)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    severity = Column(String(50), default="medium")
    source = Column(String(100))
    status = Column(String(50), default="new")
    created_at = Column(DateTime, default=datetime.utcnow)


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    severity = Column(String(50), default="medium")
    status = Column(String(50), default="open")
    investigation_notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class Risk(Base):
    __tablename__ = "risks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    likelihood = Column(Integer, default=1)
    impact = Column(Integer, default=1)
    risk_score = Column(Integer, default=1)
    mitigation = Column(Text)
    status = Column(String(50), default="identified")
    created_at = Column(DateTime, default=datetime.utcnow)
