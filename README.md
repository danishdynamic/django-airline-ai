# Django Airline AI

[![Django](https://img.shields.io/badge/Django-5.2.8-green)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.16.1-blue)](https://www.django-rest-framework.org/)
[![Celery](https://img.shields.io/badge/Celery-5.6.0-orange)](https://docs.celeryproject.org/)
[![Redis](https://img.shields.io/badge/Redis-7.2.4-red)](https://redis.io/)
[![SQLite](https://img.shields.io/badge/SQLite-3.45.1-blue)](https://www.sqlite.org/)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0.0-green)](https://www.openapis.org/)
[![VADER](https://img.shields.io/badge/VADER-Sentiment%20Analysis-yellow)](https://github.com/cjhutto/vaderSentiment)
[![Docker](https://img.shields.io/badge/Docker-20.10.17-blue)](https://www.docker.com/)

## Overview
The Django Airline AI application allows users to register, log in, and manage flight information. Users can add, edit, and delete flights, as well as submit reviews for each flight. The reviews are analyzed for sentiment using the VADER sentiment analysis tool, and the results are stored in the database. The application uses Celery for asynchronous task processing, particularly for analyzing the sentiment of flight reviews using the VADER sentiment analysis tool.

![Demo GIF Description](/images/demo_curd.mp4)


## Features

| Feature | Description |
|---------|-------------|
| User Authentication | Secure login and registration system |
| Flight Management | Add, edit, and delete flight information |
| Review System | Submit and manage flight reviews with AI sentiment analysis |
| Asynchronous Processing | Celery-based background tasks for sentiment analysis |
| Real-time Monitoring | Flower dashboard for Celery task monitoring |
| REST API | Full RESTful API with OpenAPI documentation |

> **Note:** The sentiment analysis uses VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze review comments and provide positive, negative, or neutral sentiment scores.
- RESTful API with Django Rest Framework
- Interactive API documentation with drf-spectacular
- Sentiment analysis using VADER
- Periodic cleanup of old sentiment data
- docker support for easy deployment
  

## Requirements
- Python 3.x
- Django
- Django Rest Framework
- drf-spectacular
- VADER Sentiment Analysis
- Docker and Docker Compose (optional, for containerization)
- Celery
- Redis (as a message broker)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/danishdynamic/django-airline-ai.git
   cd django-airline-ai
   ```


2. To run manually:
   - Create a virtual environment:
     ```bash
     python -m venv env
     source env/bin/activate  # On Windows use `env\Scripts\activate`
     ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Set up the database:
     ```bash
     python manage.py migrate
     ```
   - Run the Redis server (if not using Docker):
     ```bash
     redis-server
     ```
     Or using Docker:
     ```bash
     docker run -d -p 6379:6379 redis:alpine
     ```
   - Start the Celery worker:
     ```bash
     celery -A airline worker --loglevel=info
     ```
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```

## Usage

Navigate to `http://127.0.0.1:8000` in your web browser to access the application. Use the provided forms to manage flights and reviews.

### Example API Request

```bash
# Create a new review
curl -X POST http://127.0.0.1:8000/api/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "flight": 1,
    "name": "John Doe",
    "rating": 5,
    "comment": "Excellent flight experience!"
  }'
```

> **Tip:** The sentiment analysis happens asynchronously, so review sentiment data may take a moment to appear after submission.

## API Documentation

This project includes a RESTful API built with Django Rest Framework (DRF).

## Docker Support

The application can be easily containerized using Docker and Docker Compose. The provided `docker-compose.yml` file sets up the Django application, Redis, Celery worker, and Flower monitoring dashboard.

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/reviews/` | GET | List all reviews |
| `/api/reviews/` | POST | Create a new review |
| `/api/reviews/{id}/` | GET | Retrieve a specific review |
| `/api/reviews/{id}/` | PUT | Update a specific review |
| `/api/reviews/{id}/` | DELETE | Delete a specific review |

> **API Usage:** All endpoints support JSON data format. Authentication may be required for certain operations.  

### Documentation

The API documentation is generated using [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/). You can access the interactive API documentation at:

![OpenAPI Documentation Screenshot](images/Openapi-api-docs-.png)

- **Swagger UI**: `http://127.0.0.1:8000/api/schema/swagger-ui/`
  
- **ReDoc**: `http://127.0.0.1:8000/api/schema/redoc/`

- **Flower** : using flower for monitoring celery tasks at: `http://127.0.0.1:5555`

![Flower Monitoring Dashboard](images/2025-flower-1.png)

Make sure to run the server to access the documentation.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Django Rest framework
- Celery for task management
- Redis for message brokering
- VADER for sentiment analysis
- docker and docker-compose for containerization

## Future Improvements

- Implement autoscaling and load balancing using AWS or similar cloud services to enhance performance and reliability under varying loads.

## Images

All PNG images and demo are stored in the `images` folder.