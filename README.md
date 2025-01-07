# Identity_Reconciliation
 This project is a Python-based SQLite solution for the e-commerce platform Zamazon.com, designed to reconcile and manage customer contact identities. It connects multiple records with different contact information to a single individual, ensuring precise tracking of orders and customer data.



## Tech Stack

-**Python Version**: 3
- **Backend Framework**: Flask
- **Database**: SQLite (using SQLAlchemy for ORM)
  
- **Libraries**:
  - Flask
  - Flask-SQLAlchemy


## Installation Guide

Follow these steps to set up the project locally:

### Step 1: Clone the Repository
```plaintext
git clone https://github.com/arjun-mighty/Identity_Reconciliation.git
cd Identity_Reconciliation
```

### Step 2: Install Dependencies

Install the required Python packages using pip:
```plaintext
pip install Flask-SQLAlchemy flask
or
pip3 install Flask-SQLAlchemy flask
```

### Step 3: Initialize the Database

The database is automatically initialized when you run the application. However, if you want to manually create the database schema, you can call the `init_db` function in your code.

### Step 5: Run the Application

Run the Flask application:
```plaintext
python -m app
or 
python3 -m app
```
The application will start on `http://127.0.0.1:5000/`.

# Testing the API with Postman

You can use Postman to test the `POST /identify` API endpoint for identity reconciliation.

## Steps to Test with Postman

### 1. Open Postman
- Download and open the Postman application if you haven't already.
- https://www.postman.com/downloads/
  
### 2. Create a New Request
- Click on **New** > **Request**.
- Name the request (e.g., "Identify Contact") and save it to a collection if desired.

### 3. Set the Request Type and URL
- Set the request type to **POST**.
- Enter the URL: `http://localhost:3000/identify`.

### 4. Configure the Request Body
- In the **Body** tab, select **raw** and choose **JSON** from the dropdown.
- Enter the JSON payload as shown below:
  
```plaintext
 {
"email": "user1@example.com",
"phoneNumber": 1234567890
}
```
### 5. Send the Request
- Click **Send** to submit the request.



### 6. View the Response
You should receive a JSON response with the following format if the server is running correctly:
```plaintext
{
"primaryContactId": 1,
"emails": ["user1@example.com"],
"phoneNumbers": [1234567890],
"secondaryContactIds": []
}
```
This confirms that your API is working as expected. You can adjust the request body to test with different email and phone numbers, observing how the service reconciles contacts.

## Current Date
Tuesday, January 07, 2025, 12 PM IST

## Author

[Arjun_Budda](https://github.com/arjun-mighty)
