# Project Documentation

## 📌 Project Setup

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python 3.8
- Django 4.2
- Postgresql 17
- pip
- virtualenv

### 2️⃣ Clone the Repository
```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 3️⃣ Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---
## 🌍 Environment Variables (.env)
Using a `.env` file helps manage sensitive configuration variables securely. 

### 1 Create a `.env` File
Copy the `.env.example` file and modify only the database settings and secret key:
```bash
cp .env.example .env
```
Then, update the `.env` file with your actual values:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 2 `.env.example` File
For reference, `.env.example` should contain placeholders:
```ini
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_NAME=your_db_name_here
DATABASE_USER=your_db_user_here
DATABASE_PASSWORD=your_db_password_here
DATABASE_HOST=localhost
DATABASE_PORT=5432
```


### 5️⃣ Apply Migrations
```bash
python manage.py migrate
```

---
## 🔄 Loading Database Backup
To restore data from a JSON backup:
```bash
python manage.py loaddata backup.json
```

> Ensure `backup.json` is inside the project directory or provide the full path.


## 🔄 Dump Database Backup if essential anytime
To dump data to a JSON backup:
```bash
python manage.py dumpdata > backup.json
```

---
## 🔐 Authentication Using Bearer Token

### 1️⃣ Obtain Access Token
Send a POST request to obtain a token:
```bash
curl -X POST http://127.0.0.1:8000/userapi/login/ -H "Content-Type: application/json" -d '{"email": "user_email", "password": "your_password"}'
```
_Response:_
```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```

### 2️⃣ Use Bearer Token in Requests
Include the token in the `Authorization` header:
```bash
curl -X GET http://127.0.0.1:8000/api/protected-endpoint/ \
     -H "Authorization: Bearer your_access_token"
```

### 3️⃣ Authenticate in Swagger UI
To use authentication in Swagger UI, follow these steps:
1. Open Swagger at: `http://127.0.0.1:8000/`
2. Click on the **Authorize** button.
3. In the input field, enter your token in the format:
   ```
   Bearer your_access_token
   ```
4. Click **Authorize** and close the dialog.
5. Now, Swagger will include the token in API requests.

### 4️⃣ Refresh Token
To refresh an expired token:
```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ -H "Content-Type: application/json" -d '{"refresh": "your_refresh_token"}'
```


---
## 🚀 Running the Development Server
```bash
python manage.py runserver
```

Server will start at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---
## 🛠 API Documentation
```
http://127.0.0.1:8000/
```
For ReDoc:
```
http://127.0.0.1:8000/redoc/
```

---
## 📝 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
## 🏗 Contributing
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---
## 📞 Contact
For queries, contact: `media.amirhamja@gmail.com`









