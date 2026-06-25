from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database.connection import Base
from sqlalchemy.orm import relationship

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    serial_number = Column(String(50), unique=True, nullable=False, index=True)
    device_type = Column(String(50), nullable=False)  # laptop, tablet, proyector, etc.
    brand = Column(String(50), nullable=True)
    is_available = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relación con préstamos
    loans = relationship("Loan", back_populates="device", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Device(id={self.id}, name={self.name}, serial={self.serial_number})>"