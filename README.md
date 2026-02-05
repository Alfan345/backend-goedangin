# 🏬 Goedangin - Backend API

> RESTful API backend untuk aplikasi manajemen gudang/inventori dengan fitur prediksi Machine Learning

[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Hapi.js](https://img.shields.io/badge/Hapi.js-21.3-orange.svg)](https://hapi.dev/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black.svg)](https://flask.palletsprojects.com/)
[![Google Cloud](https://img.shields.io/badge/GCP-App%20Engine-4285F4.svg)](https://cloud.google.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1.svg)](https://www.mysql.com/)

---

## 📌 **Project Overview**

**Goedangin** adalah sistem backend untuk aplikasi manajemen gudang (warehouse management) yang dilengkapi dengan:

- 🔐 **Authentication & Authorization** - JWT-based secure access
- 📦 **Inventory Management** - CRUD operations untuk barang
- 🤖 **ML Prediction API** - Prediksi demand/stok menggunakan TensorFlow
- ☁️ **Cloud Deployment** - Production-ready di Google Cloud Platform
- 📄 **PDF Generation** - Generate laporan inventori
- 📱 **SMS Notification** - Twilio integration untuk notifikasi

---

## 🚀 **Key Features**

### **Main Backend (Node.js/Hapi.js)**
✅ **User Authentication**
- JWT token-based authentication
- Password hashing with bcrypt
- Secure credential management

✅ **Inventory Management**
- Create, Read, Update, Delete (CRUD) barang
- Stock tracking & management
- Category & warehouse management

✅ **Additional Features**
- PDF report generation (PDFKit, PDFMake)
- SMS notifications (Twilio)
- Input validation (Joi)
- CORS enabled

### **ML Prediction API (Python/Flask)**
✅ **Demand Forecasting**
- TensorFlow model untuk prediksi stok
- Time-series prediction
- Historical data analysis

✅ **Database Integration**
- SQLAlchemy ORM
- MySQL connection pooling
- Prediction result storage

---

## 📂 **Architecture**

### **Microservices Architecture**

```
┌─────────────────┐
│   Mobile App    │
│   (Frontend)    │
└────────┬────────┘
         │
         ├──────────────┬──────────────┐
         │              │              │
    ┌────▼─────┐  ┌────▼──────┐  ┌───▼───────┐
    │ Auth API │  │  Main API │  │  ML API   │
    │ (Hapi.js)│  │ (Hapi.js) │  │  (Flask)  │
    └────┬─────┘  └─────┬─────┘  └─────┬─────┘
         │              │              │
         └──────────────┼──────────────┘
                        │
                  ┌─────▼──────┐
                  │  Cloud SQL │
                  │   (MySQL)  │
                  └────────────┘
```

---

## 🛠️ **Tech Stack Details**

### **Main Backend (app-main/)**

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | Hapi.js 21.3 | REST API server |
| **Authentication** | @hapi/jwt | JWT token management |
| **Database** | MySQL 8.0 | Cloud SQL database |
| **ORM/Query** | mysql2 | MySQL client |
| **Validation** | Joi | Request validation |
| **Security** | bcrypt | Password hashing |
| **Notifications** | Twilio | SMS alerts |
| **File Generation** | PDFKit, PDFMake | PDF reports |
| **Cloud** | Google Cloud Platform | App Engine deployment |

**Key Dependencies:**
```json
{
  "@hapi/hapi": "^21.3.12",
  "@hapi/jwt": "^3.2.0",
  "mysql2": "^3.11.5",
  "bcrypt": "^5.1.1",
  "joi": "^17.13.3",
  "jsonwebtoken": "^9.0.2",
  "twilio": "^5.3.6",
  "pdfkit": "^0.15.1",
  "axios": "^1.7.8"
}
```

### **ML API (ML-api/)**

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Web Framework** | Flask | Lightweight API server |
| **ML Framework** | TensorFlow | Prediction model |
| **Data Processing** | Pandas, NumPy | Data manipulation |
| **Database** | SQLAlchemy | ORM for MySQL |
| **Cloud Storage** | Google Cloud Storage | Model storage |

**Key Dependencies:**
```txt
Flask==3.1.0
tensorflow==2.18.0
pandas==2.2.3
sqlalchemy==2.0.36
google-cloud-storage==2.19.0
```

---

## 💻 **Installation & Setup**

### **Prerequisites**
```bash
- Node.js 18+
- Python 3.11+
- MySQL 8.0+
- Google Cloud SDK (for deployment)
```

### **1. Clone Repository**
```bash
git clone https://github.com/Alfan345/backend-goedangin.git
cd backend-goedangin
```

### **2. Setup Main Backend**

```bash
cd app-main

# Install dependencies
npm install

# Setup environment variables
cp .env.example .env
# Edit .env with your credentials
```

**Environment Variables (.env):**
```env
PORT=4000
SECRET_KEY=your-jwt-secret-key
DB_HOST=your-database-host
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_NAME=your-database-name
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
```

### **3. Setup ML API**

```bash
cd ML-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### **4. Database Setup**

```bash
# Create database
mysql -u root -p
CREATE DATABASE goedangin;
USE goedangin;

# Run migrations (if available)
# Import schema atau jalankan migration scripts
```

### **5. Run Locally**

**Main Backend:**
```bash
cd app-main
npm start
# Server running on http://localhost:4000
```

**ML API:**
```bash
cd ML-api
python main.py
# API running on http://localhost:8080
```

---

## 🔌 **API Endpoints**

### **Authentication API**

#### **POST /auth/register**
Register new user
```json
// Request
{
  "email": "user@example.com",
  "password": "securePassword123",
  "name": "John Doe",
  "phone": "+628123456789"
}

// Response
{
  "status": "success",
  "message": "User registered successfully",
  "data": {
    "userId": 1,
    "email": "user@example.com"
  }
}
```

#### **POST /auth/login**
User login
```json
// Request
{
  "email": "user@example.com",
  "password": "securePassword123"
}

// Response
{
  "status": "success",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "email": "user@example.com",
      "name": "John Doe"
    }
  }
}
```

---

### **Inventory Management API**

#### **GET /items**
Get all inventory items
```bash
curl -H "Authorization: Bearer <token>" \
  http://localhost:4000/items
```

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Product A",
      "sku": "PRD-001",
      "quantity": 150,
      "category": "Electronics",
      "price": 250000,
      "warehouse": "Gudang Pusat"
    }
  ]
}
```

#### **POST /items**
Add new item
```json
// Request
{
  "name": "Product B",
  "sku": "PRD-002",
  "quantity": 100,
  "category": "Furniture",
  "price": 500000,
  "warehouse": "Gudang Cabang"
}
```

#### **PUT /items/{id}**
Update item

#### **DELETE /items/{id}**
Delete item

---

### **ML Prediction API**

#### **POST /predict**
Generate stock prediction
```bash
curl -X POST http://localhost:8080/predict
```

**Response:**
```json
{
  "status": "success",
  "predictions": [
    {
      "item_id": 1,
      "item_name": "Product A",
      "current_stock": 150,
      "predicted_demand": 75,
      "predicted_date": "2026-03-05",
      "recommendation": "Maintain current stock"
    }
  ]
}
```

#### **GET /getpredict**
Get latest predictions (last 2 results)
```bash
curl http://localhost:8080/getpredict
```

---

## ☁️ **Cloud Deployment (GCP)**

### **Deploy Main Backend**

```bash
cd app-main
gcloud app deploy app.yaml
```

**app.yaml configuration:**
```yaml
runtime: nodejs18
env: standard
instance_class: F2
```

### **Deploy ML API**

```bash
cd ML-api
gcloud app deploy app.yaml --version ml-api
```

**app.yaml configuration:**
```yaml
runtime: python311
env: standard
instance_class: F2
entrypoint: python main.py
```

### **Cloud SQL Setup**

```bash
# Create Cloud SQL instance
gcloud sql instances create goedangin-db \
  --database-version=MYSQL_8_0 \
  --tier=db-f1-micro \
  --region=asia-southeast2

# Create database
gcloud sql databases create goedangin --instance=goedangin-db

# Connect using Cloud SQL Proxy
./cloud_sql_proxy -instances=<INSTANCE_CONNECTION_NAME>=tcp:3306
```

---

## 🔒 **Security**

### **Implemented Security Measures:**

✅ **Authentication & Authorization**
- JWT token with expiration
- Password hashing (bcrypt)
- Secure credential storage

✅ **Database Security**
- Prepared statements (SQL injection prevention)
- Connection pooling
- Cloud SQL IAM authentication

✅ **API Security**
- CORS configuration
- Input validation (Joi)
- Rate limiting (optional - add later)

✅ **Environment Variables**
- Sensitive data in .env
- .gitignore for credentials
- Google Secret Manager (production)

---

## 📊 **Database Schema**

### **Users Table**
```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Items Table**
```sql
CREATE TABLE items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  sku VARCHAR(50) UNIQUE NOT NULL,
  quantity INT DEFAULT 0,
  category VARCHAR(100),
  price DECIMAL(15,2),
  warehouse VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### **Predictions Table**
```sql
CREATE TABLE predictions (
  id INT AUTO_INCREMENT PRIMARY KEY,
  item_id INT,
  predicted_demand INT,
  prediction_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (item_id) REFERENCES items(id)
);
```

---

## 🎓 **Skills Demonstrated**

| Category | Skills |
|----------|--------|
| **Backend Development** | Node.js, Hapi.js, RESTful API, Microservices |
| **Python Development** | Flask, TensorFlow, Data Processing |
| **Database** | MySQL, Cloud SQL, SQLAlchemy, Query Optimization |
| **Authentication** | JWT, bcrypt, Token management |
| **Cloud Computing** | Google Cloud Platform, App Engine, Cloud SQL |
| **DevOps** | Deployment automation, Environment management |
| **API Design** | REST principles, Validation, Error handling |
| **Security** | Authentication, Authorization, Data protection |
| **Integration** | Twilio SMS, PDF generation, External APIs |
| **Machine Learning** | TensorFlow, Prediction models, Data analysis |

---

## 📈 **Project Structure Explained**

### **app-main/src/**
```
src/
├── auth/
│   ├── routes.js          # Authentication routes
│   ├── handler.js         # Auth business logic
│   └── validation.js      # Input validation schemas
│
├── management/
│   ├── routes.js          # Inventory routes
│   ├── handler.js         # Inventory logic
│   └── validation.js      # Validation schemas
│
├── middlewares/
│   └── auth.js            # JWT verification middleware
│
├── utils/
│   ├── pdf.js             # PDF generation utilities
│   ├── sms.js             # Twilio integration
│   └── helpers.js         # Common helper functions
│
└── database.js            # Database connection pool
```

### **ML-api/**
```
ML-api/
├── main.py                # Flask API endpoints
├── utils.py               # Prediction utilities
├── requirements.txt       # Python dependencies
└── app.yaml              # GCP deployment config
```

---

## 🔧 **Configuration Files**

### **package.json**
```json
{
  "name": "goedangin-backend",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  }
}
```

### **requirements.txt**
```txt
Flask==3.1.0
tensorflow==2.18.0
pandas==2.2.3
sqlalchemy==2.0.36
pymysql==1.1.1
google-cloud-storage==2.19.0
```

---

## 🚧 **Future Enhancements**

- [ ] Add rate limiting & throttling
- [ ] Implement caching (Redis)
- [ ] Add API documentation (Swagger/OpenAPI)
- [ ] Implement WebSocket for real-time updates
- [ ] Add unit & integration tests
- [ ] Implement CI/CD pipeline
- [ ] Add monitoring & logging (Cloud Logging)
- [ ] Implement role-based access control (RBAC)
- [ ] Add GraphQL endpoint
- [ ] Implement file upload for product images

---

## 🐛 **Troubleshooting**

### **Database Connection Issues**
```bash
# Test Cloud SQL Proxy connection
./cloud_sql_proxy -instances=<INSTANCE_CONNECTION_NAME>=tcp:3306

# Verify MySQL connection
mysql -h 127.0.0.1 -u root -p
```

### **JWT Token Errors**
```javascript
// Verify SECRET_KEY in .env
console.log(process.env.SECRET_KEY);

// Check token expiration
jwt.verify(token, SECRET_KEY);
```

### **ML API Errors**
```python
# Check TensorFlow installation
import tensorflow as tf
print(tf.__version__)

# Verify database connection
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://user:pass@host/db')
```

---

## 📚 **Additional Resources**

- [Hapi.js Documentation](https://hapi.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [TensorFlow Guide](https://www.tensorflow.org/guide)
- [Google Cloud Platform](https://cloud.google.com/docs)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

## 👤 **Author**

**Alfanah Muhson**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/alfanah-muhson)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/Alfan345)

---

## 📝 **License**

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 **Acknowledgments**

- Hapi.js team untuk framework yang powerful
- TensorFlow team untuk ML framework
- Google Cloud Platform untuk cloud infrastructure
- Twilio untuk SMS notification service

---

**⭐ If you find this project useful, please give it a star!**

---

## 🎯 **Use Case**

Project ini cocok untuk:
- 🏪 **Retail Management** - Manajemen stok toko retail
- 🏭 **Warehouse Management** - Sistem gudang perusahaan
- 📦 **E-commerce Backend** - Backend untuk platform e-commerce
- 📊 **Inventory Analytics** - Analisis dan prediksi inventori

---

**💡 Note:** Repository ini merupakan bagian dari project capstone/final project untuk aplikasi Goedangin - sistem manajemen gudang yang terintegrasi dengan machine learning untuk prediksi demand.
