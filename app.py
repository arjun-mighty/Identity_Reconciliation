from flask import Flask, request, jsonify
from database import db, Contact, init_db

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
init_db(app)

@app.route('/identify', methods=['POST'])
def identify():
    data = request.get_json()
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')

    if not email and not phoneNumber:
        return jsonify({"error": "Email or phone number must be provided."}), 400

    matching_contacts = Contact.query.filter(
        (Contact.email == email) & (Contact.phoneNumber == phoneNumber)
    ).first()

    if matching_contacts:
        return jsonify({"message": "Alredy exists"}), 200

    # Query matching contacts
    matching_contacts = Contact.query.filter(
        (Contact.email == email) | (Contact.phoneNumber == phoneNumber)
    ).all()

    if not matching_contacts:
        # Create a new primary contact
        new_contact = Contact(email=email, phoneNumber=phoneNumber, linkPrecedence="primary")
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({
            "primaryContactId": new_contact.id,
            "emails": [new_contact.email],
            "phoneNumbers": [new_contact.phoneNumber],
            "secondaryContactIds": []
        }), 200

    # Process existing contacts
    primary_contact = None
    secondary_contacts = []
    emails = set()
    phoneNumbers = set()

    for contact in matching_contacts:
        emails.add(contact.email)
        phoneNumbers.add(contact.phoneNumber)
        if contact.linkPrecedence == "primary" and not primary_contact:
            primary_contact = contact
        else:
            secondary_contacts.append(contact)

    if not primary_contact:
        primary_contact = matching_contacts[0]
        primary_contact.linkPrecedence = "primary"
        db.session.commit()

    if email and email not in emails:
        new_secondary = Contact(email=email, phoneNumber=None, linkedId=primary_contact.id, linkPrecedence="secondary")
        db.session.add(new_secondary)
        db.session.commit()
        secondary_contacts.append(new_secondary)
        emails.add(email)

    if phoneNumber and phoneNumber not in phoneNumbers:
        new_secondary = Contact(email=None, phoneNumber=phoneNumber, linkedId=primary_contact.id, linkPrecedence="secondary")
        db.session.add(new_secondary)
        db.session.commit()
        secondary_contacts.append(new_secondary)
        phoneNumbers.add(phoneNumber)

    return jsonify({
        "primaryContactId": primary_contact.id,
        "emails": list(emails),
        "phoneNumbers": list(phoneNumbers),
        "secondaryContactIds": [contact.id for contact in secondary_contacts]
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
