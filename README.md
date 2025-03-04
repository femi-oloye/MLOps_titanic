# Titanic Survival Prediction API

This project is part of my MLOps portfolio, implementing a machine learning model to predict Titanic passenger survival. The model is deployed as an API using FastAPI, Docker, and AWS EC2.

## Features
- Logistic Regression model trained on the Titanic dataset
- API built using FastAPI
- Dockerized application
- Deployed on AWS EC2 with Docker

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-github-username/MLOps_titanic.git
cd MLOps_titanic
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model
```bash
python train_model.py
```
This will generate the model file `titanic_model.pkl` inside the `model/` directory.

### 4. Run the API Locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 5. Build and Run with Docker
```bash
docker build -t titanic-api .
docker run -d --restart always -p 8000:8000 titanic-api
```

### 6. Deploy on AWS EC2
Ensure Docker is installed on your EC2 instance and run:
```bash
docker pull your-dockerhub-username/titanic-api

docker run -d --restart always -p 8000:8000 your-dockerhub-username/titanic-api
```

## API Endpoints

### 1. Homepage
```bash
GET /
```
Response:
```json
{"message": "This is the homepage of the API"}
```

### 2. Predict Survival
```bash
POST /predict
```
#### Example Input (JSON):
```json
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}
```
#### Example Output (JSON):
```json
{"survived": 0}
```

## Future Improvements
- Implement a CI/CD pipeline with GitHub Actions
- Add model monitoring and logging
- Improve model performance with feature engineering

---

## Author
oluwafemi oloye - [GitHub Profile](https://github.com/femi-oloye)

