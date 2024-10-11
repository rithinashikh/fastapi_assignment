# FastAPI CRUD Application

This is a FastAPI project implementing CRUD operations for **Items** and **User Clock-In Records**. The project is designed as part of an assignment for Vodex.ai. It performs various operations such as creating, retrieving, updating, and deleting data with MongoDB. The project also includes filtering and aggregation operations for data retrieval.

## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Database Configuration](#database-configuration)
- [Available Endpoints](#available-endpoints)
- [Running Locally](#running-locally)
- [Hosted Application](#hosted-application)
- [Technologies Used](#technologies-used)

## Setup Instructions

### Prerequisites

1. **Python 3.7+**: You need Python installed on your system.
2. **MongoDB Atlas**: Create an account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or install MongoDB locally.
3. **FastAPI**: Install FastAPI and other necessary packages.
4. **Koyeb/Heroku**: Host the application on a free hosting platform.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/fastapi-crud-app.git
   cd fastapi-crud-app

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Set up environment variables for MongoDB connection in a .env file:

    ```bash
    MONGO_URI="your-mongodb-uri"

## Database Configuration

You will need to create two collections in MongoDB for the two entities:

- items
- clock_in_records

Refer to the MongoDB Atlas documentation to set up the database and collections if you are using MongoDB Atlas.

## Available Endpoints

### Items APIs
1. POST /items
- Create a new item.

Request Body:
json

    {
    "name": "John Doe",
    "email": "john@example.com",
    "item_name": "Laptop",
    "quantity": 5,
    "expiry_date": "2024-12-31"
    }

2. GET /items/{id}
- Retrieve an item by its ID.

3. GET /items/filter
- Filter items based on:

    - email: Exact match.
    - expiry_date: Filter items expiring after the provided date.
    - insert_date: Filter items inserted after the provided date.
    - quantity: Items with quantity greater than or equal to the provided number.

4. GET /items/aggregate
- Aggregate data to return the count of items for each email.

5. PUT /items/{id}
- Update an item’s details by ID.

6. DELETE /items/{id}
Delete an item by its ID.

### Clock-In Records APIs
1. POST /clock-in
- Create a new clock-in record.

Request Body:
json

    {
    "email": "john@example.com",
    "location": "New York"
    }

2. GET /clock-in/{id}
- Retrieve a clock-in record by its ID.

3. GET /clock-in/filter
- Filter clock-in records based on:

    - email: Exact match.
    - location: Exact match.
    - insert_datetime: Filter records created after the provided date.
4. PUT /clock-in/{id}
- Update a clock-in record by its ID.

5. DELETE /clock-in/{id}
- Delete a clock-in record by its ID.

## Running Locally

Start the FastAPI application:

    uvicorn main:app --reload
Access the API documentation in your browser:


http://127.0.0.1:8000/docs

## Hosted Application
The application is hosted on a free platform:

Swagger Documentation: 


### Technologies Used
- ***FastAPI:*** A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- ***MongoDB:*** A NoSQL database for storing Items and Clock-In Records.
- ***Pydantic:*** For data validation and parsing.
- ***Uvicorn:*** ASGI server to run FastAPI apps.
- ***Koyeb:*** Free hosting platform for deploying the application.