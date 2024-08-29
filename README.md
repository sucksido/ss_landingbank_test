Here is a sample `README.md` file that includes instructions for installation, running, and testing the API:

---

# Holiday Planner Weather API

This project is a Django REST API that allows users to retrieve weather data for specific locations. The weather data is fetched from the Open-Meteo API based on latitude and longitude parameters provided by the user.

## Table of Contents
- [Installation](#installation)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.8 or higher
- pip (Python package installer)
- Docker (optional, for containerized setup)

### Clone the Repository

```bash
git clone https://github.com/sucksido/holiday-planner-api.git
cd holiday-planner-api
```

### Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv holiday_planner_env
source holiday_planner_env/bin/activate  # On Windows use `holiday_planner_env\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the API

### Apply Migrations

Before running the server, apply the migrations:

```bash
python manage.py migrate
```

### Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

- **GET `/api/weather/`**

  This endpoint retrieves weather data for a specific location.

  **Query Parameters:**
  - `latitude`: The latitude of the location.
  - `longitude`: The longitude of the location.
  - `days` (optional): The number of days to forecast (default is 7 days).

  **Example Request:**

  ```
  GET /api/weather/?latitude=52.52&longitude=13.41&days=7
  ```

  **Example Response:**

  ```json
  [
      {
          "date": "2024-08-29T00:00:00Z",
          "temperature_2m": 20.5
      },
      {
          "date": "2024-08-30T00:00:00Z",
          "temperature_2m": 21.0
      }
  ]
  ```

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

This will run all unit tests and output the results to the terminal.

## Docker Setup

If you prefer to run the API inside a Docker container, follow these steps:

### Build the Docker Image

```bash
docker-compose build
```

### Run the Docker Container

```bash
docker-compose up
```

The API will be accessible at `http://127.0.0.1:8000/` within the Docker environment.

## Troubleshooting

### Common Issues

- **ModuleNotFoundError**: Ensure your virtual environment is activated and all dependencies are installed via `pip install -r requirements.txt`.
- **Database Errors**: Make sure you've applied all migrations with `python manage.py migrate`.

![image](https://github.com/user-attachments/assets/3374a658-8d40-4f97-ba7f-044560a12e2e)
