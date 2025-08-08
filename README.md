\# BigQuery Data Pipeline on Google Cloud



\## 📌 Overview

This project demonstrates a data pipeline on Google Cloud using Cloud Storage, Dataflow, and BigQuery. 

It loads sample data from Cloud Storage, processes it using Dataflow, and loads the processed data into BigQuery for analytics.



\## 🚀 Features

\- Data ingestion from CSV in Cloud Storage

\- Data processing and transformation with Apache Beam (Dataflow)

\- Loading cleaned data into BigQuery

\- Visualization with Looker Studio (optional)



\## 🛠 Tech Stack

\- Google Cloud Storage (GCS)

\- Google Dataflow (Apache Beam)

\- BigQuery

\- Python 3



\## 📂 Architecture

!\[Architecture Diagram](architecture.png)



\## ⚙️ Setup \& Deployment



1\. \*\*Enable APIs\*\*

```bash

gcloud services enable dataflow.googleapis.com bigquery.googleapis.com storage.googleapis.com



