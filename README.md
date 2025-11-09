# 🛒 Retail Sales ETL Pipeline (CSV → S3 → PostgreSQL)

## 📘 Overview
This project demonstrates a **classic data engineering ETL pipeline** built with Python, PostgreSQL, and AWS S3.  
The goal is to automate the process of **extracting**, **cleaning**, **transforming**, and **loading** retail sales data for analytical reporting.

It simulates a real-world data flow where monthly sales CSVs are cleaned and consolidated into a structured PostgreSQL database for BI dashboards or SQL analysis.

---

## 🧩 Tech Stack
- **Language:** Python (pandas, numpy)
- **Database:** PostgreSQL (SQLAlchemy + psycopg2)
- **Cloud Storage:** AWS S3 (boto3)
- **Environment Management:** dotenv
- **Data Format:** CSV → PostgreSQL Table
- **ETL Architecture:** Extract → Transform → Load

---

## 🏗️ Architecture Diagram

      +-----------------+
      | Monthly CSVs    |
      | (raw data)      |
      +--------+--------+
               |
               v
      [ Extract with pandas ]
               |
               v
      +-----------------+
      | Clean & Standard|
      | using pandas/numpy |
      +--------+--------+
               |
               v
      [ Upload to AWS S3 ]
               |
               v
      +-----------------+
      | PostgreSQL DB   |
      | fact_sales table|
      +--------+--------+
               |
               v
      [ SQL Analytics ]
               |
               v
      +-----------------+
      | BI / Dashboard  |
      +-----------------+


---

## 📂 Project Structure

retail-sales-etl-pipeline/
├─ data/
│ ├─ raw/ # Unprocessed CSVs (gitignored)
│ └─ processed/ # Cleaned and combined data
├─ sql/
│ ├─ create_table.sql # PostgreSQL schema
│ └─ analytics_queries.sql # Example business queries
├─ src/
│ ├─ config.py # Environment variables
│ ├─ extract.py # Read & combine CSVs
│ ├─ transform.py # Clean and standardize data
│ ├─ load.py # Upload to S3 + PostgreSQL
│ └─ run_pipeline.py # Orchestrates ETL
├─ .env.example # Example environment config
├─ requirements.txt
├─ .gitignore
└─ README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Pondcod/retail-sales-etl-pipeline.git
cd retail-sales-etl-pipeline
