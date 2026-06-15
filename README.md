# AI Recipe Generator

## Project Overview

AI Recipe Generator is a web-based application that generates cooking recipes from ingredients provided by the user. The application uses an AI language model to create realistic recipes and presents them through an interactive web interface.

## Objective

The purpose of this project is to demonstrate how Artificial Intelligence can be integrated into a web application to solve a real-world problem. Users can enter available ingredients and receive recipe suggestions instantly.

## Features

- Generate recipes from user-provided ingredients
- AI-powered recipe generation
- FastAPI backend API
- Streamlit web interface
- Simple and user-friendly design
- PDF recipe export

## Technologies Used

### Frontend
- Streamlit

### Backend
- FastAPI
- Pydantic

### AI Model
- Google FLAN-T5 Base
- Hugging Face Transformers

### Programming Language
- Python

## Project Structure

text project/ │ ├── backend/ │   └── api.py │ ├── frontend/ │   └── app.py │ ├── requirements.txt ├── README.md └── screenshots/ 

## Installation

### Clone Repository

bash git clone https://github.com/rpahata/ai-recipe-generator.git cd ai-recipe-generator 

### Create Virtual Environment

bash python -m venv venv 

### Activate Virtual Environment

Mac/Linux:

bash source venv/bin/activate 

Windows:

bash venv\Scripts\activate 

### Install Dependencies

bash pip install -r requirements.txt 

## Running the Application

### Start FastAPI Backend

bash uvicorn backend.api:app --reload 

Backend URL:

text http://127.0.0.1:8000 

API Documentation:

text http://127.0.0.1:8000/docs 

### Start Streamlit Frontend

bash streamlit run frontend/app.py 

Frontend URL:

text http://localhost:8501 

## Example Usage

Input:

text chicken, rice, onion 

Output:

text Recipe Name: Chicken Rice Bowl  Ingredients: - Chicken - Rice - Onion  Steps: 1. Cook the rice. 2. Fry the onion. 3. Add chicken and cook thoroughly. 4. Mix with rice and serve. 

## Future Improvements

- Nutrition analysis
- Recipe image generation
- User accounts
- Recipe saving system
- Multiple cuisine support

## Author

Htet Wai Yan Hlaing

Programming for Data Science Final Project