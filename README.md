# topoAssessment

## Overview

This project is a **Data Ingestion and Visualization Application** built using **FastAPI** (for the backend API) and **Streamlit** (for the frontend). The application processes data from various sources (CSV, Excel, JSON, PDF, PPTX), cleans and manipulates the data, and provides endpoints to access the data in different formats.

The app also includes a **frontend** built with **Streamlit** for easy visualization and interaction with the data.

## Features

- **Data Ingestion**: The app can ingest data from CSV, Excel, JSON, PDF, and PPTX file formats.
- **Data Cleaning**: The app performs cleaning on the ingested data, handling missing values, inconsistent data types, and formatting issues.
- **API Endpoints**:
  - **GET /api/data**: Returns the full unified dataset in JSON format.
  - **GET /api/data/{file_type}**: Returns data specific to a file type (e.g., CSV, Excel).
- **Data Visualization**: Streamlit frontend provides visualizations (bar charts, line graphs, and tables) for the cleaned data.
- **Sorting and Filtering**: Interactive features to sort and filter the data on the frontend.

## Setup Instructions

Follow the steps below to run the project locally.

### Prerequisites

Ensure you have the following installed:

- **Python 3.9+** (preferably in a virtual environment).
- **pip** for installing Python packages.
- **Git** (if you are cloning the repository from GitHub).

### 1. Clone the Repository

If you're cloning from GitHub:

```bash
git clone https://github.com/HongQuan13/topoAssessment.git
cd topoAssessment
```

### 2. Install Dependencies
Install the backend dependencies:
```bash
pip install -r requirements.txt
```
### 3. Run the Application
#### Backend
Navigate to the src directory and running backend:
```bash
cd src 
uvicorn main:app --reload
```
This will start the backend API on http://127.0.0.1:8000.

#### Frontend
In another terminal window, navigate to the project root directory(topoAssessment) and run the Streamlit app:
```bash
streamlit run main.py
```
This will start the frontend on http://localhost:8501.Feel free access this to interact with the data

### API Endpoints
1. GET /api/data
This endpoint returns the full unified dataset in JSON format.

Example request:

```bash
GET http://127.0.0.1:8000/api/data
```
2. GET /api/data/{file_type}
This endpoint returns data specific to the requested file type (e.g., csv, excel, json, etc.).

Example request:

```bash
GET http://127.0.0.1:8000/api/data/csv
```
Response
The response will be a JSON object, with keys for each file type (csv, excel, json, etc.) and their corresponding cleaned data.

### Testing Instructions
1. Run Unit Tests
To run the unit tests with pytest from root project directory(topoAssessment):

```bash
pytest
```
This will run all the unit tests for the API endpoints.

### Demo video

https://drive.google.com/file/d/1dAcgrsPtEEiuGpT_IAIUABImqyPdiv5B/view?usp=sharing



