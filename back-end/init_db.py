from app import AppointmentObject, BayTable, db
import uuid

def init_db():
    db.create_all()
    test_data = BayTable('9/10/2022 7:28', '11/27/2022 7:16', 'compact')
    db.session.add(test_data)
    db.commit()
init_db()

