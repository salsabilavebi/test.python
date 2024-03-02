from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)

class ConsultationSlot(Base):
    __tablename__ = "consultation_slots"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    time = Column(String, index=True)
    availability = Column(Boolean, default=True)

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    consultation_slot_id = Column(Integer, ForeignKey("consultation_slots.id"))
    queue_number = Column(Integer)

    patient = relationship("Patient", back_populates="reservations")
    consultation_slot = relationship("ConsultationSlot", back_populates="reservations")

Patient.reservations = relationship("Reservation", back_populates="patient")
ConsultationSlot.reservations = relationship("Reservation", back_populates="consultation_slot")

# Buat semua tabel dalam database
Base.metadata.create_all(bind=engine)
class PatientCreate(BaseModel):
    name: str
    email: str
    phone_number: str

# API endpoint untuk membuat pasien baru
@app.post("/patients/")
def create_patient(patient: PatientCreate):
    db = SessionLocal()
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@app.get("/patients/")
def read_patients():
    db = SessionLocal()
    patients = db.query(Patient).all()
    return patients


@app.get("/patients/{patient_id}/")
def read_patient(patient_id: int):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


class ConsultationSlotCreate(BaseModel):
    date: str
    time: str
    availability: bool


@app.post("/consultation_slots/")
def create_consultation_slot(slot: ConsultationSlotCreate):
    db = SessionLocal()
    db_slot = ConsultationSlot(**slot.dict())
    db.add(db_slot)
    db.commit()
    db.refresh(db_slot)
    return db_slot

@app.get("/consultation_slots/")
def read_consultation_slots():
    db = SessionLocal()
    slots = db.query(ConsultationSlot).all()
    return slots


@app.get("/consultation_slots/{slot_id}/")
def read_consultation_slot(slot_id: int):
    db = SessionLocal()
    slot = db.query(ConsultationSlot).filter(ConsultationSlot.id == slot_id).first()
    if not slot:
        raise HTTPException(status_code=404, detail="Consultation slot not found")
    return slot
    

class ReservationCreate(BaseModel):
    patient_id: int
    consultation_slot_id: int


@app.post("/patients/{patient_id}/reservations/")
def create_reservation(patient_id: int, reservation: ReservationCreate):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    slot = db.query(ConsultationSlot).filter(ConsultationSlot.id == reservation.consultation_slot_id).first()
    if not slot or not slot.availability:
        raise HTTPException(status_code=400, detail="Invalid consultation slot or slot not available")

    reservation_data = Reservation(**reservation.dict(), queue_number=db.query(Reservation).count() + 1)
    db.add(reservation_data)
    db.commit()
    db.refresh(reservation_data)
    return reservation_data

@app.get("/patients/{patient_id}/reservations/")
def get_patient_reservations(patient_id: int):
    db = SessionLocal()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient.reservations


@app.put("/reservations/{reservation_id}")
def update_reservation(reservation_id: int, reservation: ReservationCreate):
    db = SessionLocal()
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    db_reservation.patient_id = reservation.patient_id
    db_reservation.consultation_slot_id = reservation.consultation_slot_id
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


@app.delete("/reservations/{reservation_id}")
def delete_reservation(reservation_id: int):
    db = SessionLocal()
    db_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    db.delete(db_reservation)
    db.commit()
    return {"message": "Reservation deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
