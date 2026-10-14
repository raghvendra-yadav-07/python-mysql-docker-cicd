# Python + MySQL Docker Application

A containerized Python application that connects to a MySQL database through a Docker network. This project demonstrates application containerization, database connectivity, environment-based configuration, and basic HTTP health checks.

## Overview

The application uses Python to serve HTTP requests and communicate with a MySQL database. Docker provides an isolated runtime environment, while a dedicated Docker network allows the application to reach the database using its container name.

## Architecture

```text
Client / Browser
       |
       | HTTP :8080
       v
+---------------------+
|  Python Container   |
|  app.py             |
|  MySQL Connector    |
+---------------------+
       |
       | Docker Network
       | MySQL :3306
       v
+---------------------+
|  MySQL Container    |
|  Database: appdb    |
+---------------------+
```

## Technology Stack

- **Python 3.12** — Application runtime
- **MySQL** — Relational database
- **Docker** — Application containerization
- **Docker Networking** — Private communication between containers
- **mysql-connector-python** — Python-to-MySQL connectivity
- **HTTP Server** — Handles application requests

## Project Structure

```text
python-mysql-docker/
├── Dockerfile
├── requirement.txt
└── src/
    └── app.py
```

> Note: The dependency filename shown above is `requirement.txt`. If your actual file is named `requirements.txt`, update the Dockerfile and this structure accordingly.

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Connects to MySQL and returns the database version |
| `/health` | Checks whether the HTTP application is running |

The `/health` endpoint checks application availability; it does not verify database connectivity.

## Configuration

The application reads its database configuration from environment variables.

| Variable | Purpose |
|---|---|
| `DB_HOST` | MySQL container hostname |
| `DB_PORT` | MySQL port, typically `3306` |
| `DB_USER` | Database username |
| `DB_PASSWORD` | Database password |
| `DB_NAME` | Database name |

Example configuration:

```text
DB_HOST=mysql
DB_PORT=3306
DB_USER=appuser
DB_NAME=appdb
```

Set `DB_PASSWORD` securely at runtime. Do not commit database passwords or other secrets to the repository.

## Docker Concepts Demonstrated

- Creating a Docker image using a Python base image
- Installing Python dependencies
- Setting a working directory inside a container
- Configuring environment variables
- Running a Python application using Docker
- Connecting application and database containers over a Docker network
- Troubleshooting application and database connectivity

## Security Considerations

- Keep database credentials out of source code.
- Do not expose the MySQL port publicly.
- Allow database access only from authorized application containers.
- Use a dedicated database user with limited privileges.
- Add persistent storage for MySQL data when required.
- Use health checks and proper error handling for production deployments.

## Learning Objectives

This project is designed to build practical skills in Python application development, Docker image creation, container networking, relational database connectivity, environment configuration, and application troubleshooting.

## Future Improvements

- Add Docker Compose for managing multiple containers.
- Add database readiness checks and connection retry logic.
- Add automated application tests.
- Add persistent MySQL storage and backup procedures.
- Add structured logging and application monitoring.
- Use a production-grade HTTP server and stronger error handling.

## Author

**Raghvendra Yadav**

Cloud & DevOps Learning Project
