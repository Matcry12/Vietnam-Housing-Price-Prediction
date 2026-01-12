# Vietnam Housing Price Prediction

This project is an end-to-end Machine Learning application for predicting housing prices in Vietnam. It includes a Jupyter Notebook for model training and analysis, and a FastAPI backend for model serving.

## Project Structure

- notebooks/
  - Vietnam Housing Price.ipynb: Main notebook for data EDA, processing, and model training.
- server/
  - server.py: FastAPI application entry point.
  - util.py: Utility functions for loading artifacts and making predictions.
- model/
  - Contains saved model artifacts (pickle, json).
- data/
  - Contains the dataset.
- client/
  - Frontend code (if applicable).

## Setup

1. Create a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

## Usage

### Training the Model
Open the notebook `notebooks/Vietnam Housing Price.ipynb` to explore the data and train the model.

### Running the API Server
To start the prediction API, run the following command from the project root:

cd server
python server.py

The API will start at http://127.0.0.1:7000.
