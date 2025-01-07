from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    linkedId = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=True)
    linkPrecedence = db.Column(db.String, nullable=False, default="primary")
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
   

    linkedContacts = db.relationship('Contact', remote_side=[id])

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()