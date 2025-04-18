# Healthcare Backend API

## Project Overview
The Healthcare Backend API is a Django-based web application designed for managing patient and doctor records in a healthcare system. This API allows users to register, log in, and manage patient and doctor records securely, with JWT-based authentication. It also includes the ability to map patients to doctors, making it an ideal backend solution for a healthcare application.

### Technologies Used:
- **Backend**: Django, Django REST Framework (DRF)
- **Database**: Supabase (PostgreSQL)
- **Authentication**: JWT (JSON Web Token) using `djangorestframework-simplejwt`
- **Environment Variables**: `.env` for secure configuration
- **Validation**: Custom error handling and validation for user inputs
- **Permissions**: Secure access control for authenticated users

## Features
1. **Authentication API**:
   - `POST /api/auth/register/`: Register a new user.
   - `POST /api/auth/login/`: Login to the system and retrieve a JWT token.

2. **Patient Management API**:
   - `POST /api/patients/`: Add a new patient (authenticated users only).
   - `GET /api/patients/`: Retrieve all patients created by the authenticated user.
   - `GET /api/patients/{id}/`: Get details of a specific patient.
   - `PUT /api/patients/{id}/`: Update a patient’s details.
   - `DELETE /api/patients/{id}/`: Delete a patient record.

3. **Doctor Management API**:
   - `POST /api/doctors/`: Add a new doctor (authenticated users only).
   - `GET /api/doctors/`: Retrieve all doctors.
   - `GET /api/doctors/{id}/`: Get details of a specific doctor.
   - `PUT /api/doctors/{id}/`: Update a doctor’s details.
   - `DELETE /api/doctors/{id}/`: Delete a doctor record.

4. **Patient-Doctor Mapping API**:
   - `POST /api/mappings/`: Assign a doctor to a patient.
   - `GET /api/mappings/`: Retrieve all patient-doctor mappings.
   - `GET /api/mappings/{patient_id}/`: Get all doctors assigned to a specific patient.
   - `DELETE /api/mappings/{id}/`: Remove a doctor from a patient.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- PostgreSQL (via Supabase)
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd healthcare-backend
```

### Step 2: Install Dependencies
```bash
python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
## Create a .env file in your project’s root directory and add the following environment variables (replace placeholders with your actual credentials):
```bash
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=supabase_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db.yoursupabasehost.supabase.co
DB_PORT=5432

```

### Step 4: Database Migration
## Set up your database schema with Django migrations:
```bash
python manage.py makemigrations
python manage.py migrate

```

### Step 5: Run the Development Server
## Start the Django development server:
```bash
python manage.py runserver

```



