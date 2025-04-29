# 📌 Travel Itinerary Management System – SDE Assignment (Stayoften)

This repository contains the backend implementation for the Full-Stack SDE Internship assignment at **Stayoften**. The system is designed to manage and recommend travel itineraries with detailed day-wise breakdowns of accommodations, transfers, and activities.

---

## ✨ Key Features

- Create detailed multi-day travel itineraries
- Store day-wise activities, hotel accommodations, and inter-location transfers
- Retrieve existing itineraries by ID
- Get recommended itineraries based on trip duration (2–8 nights)
- Designed using modular, scalable, and production-ready architecture

---

## 🛠️ Tech Stack

| Component         | Technology    |
|------------------|---------------|
| Language          | Python 3.11+   |
| Web Framework     | FastAPI        |
| ORM               | SQLAlchemy     |
| Database          | SQLite         |
| Validation        | Pydantic       |
| Server (Local)    | Uvicorn        |

---

## System Flow

## System Flow Diagram

<p align="center">
  <img src="https://github.com/user-attachments/assets/3464ef19-1da4-4a46-b8a8-195cd7958fb0" alt="System Flow" width="600"/>
</p>


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd code
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python -m uvicorn main:app --reload
```

---

Author : Yashi Gupta(yashig406@gmail.com)
