# 🐳 Two-Tier Flask Application

A containerized two-tier web application built with **Flask and MySQL**, using Docker for containerization, networking, persistent storage, health checks, and multi-container management with Docker Compose.

> **Learning Note:** This project was developed as part of my Docker and DevOps learning journey. I studied an existing two-tier Flask application and modified and extended the implementation while learning Docker, Flask, MySQL, networking, volumes, and container orchestration.

---

## 🏗️ Architecture

The application follows a simple **two-tier architecture**:

```text
        User / Browser
              │
              ▼
     ┌─────────────────┐
     │  Flask Backend   │
     │    Container     │
     │   Port: 5000     │
     └────────┬────────┘
              │
       Docker Network
              │
              ▼
     ┌─────────────────┐
     │  MySQL Database  │
     │    Container     │
     │   Port: 3306     │
     └─────────────────┘
              │
              ▼
        Docker Volume
       (Persistent Data)
```

### Tiers

**Tier 1 — Application Layer**

* Flask
* Python
* REST/Web application
* Port `5000`

**Tier 2 — Database Layer**

* MySQL
* Database persistence
* Port `3306`

---

## 🛠️ Technologies Used

* Python
* Flask
* MySQL
* Docker
* Docker Compose
* Docker Networks
* Docker Volumes
* Docker Health Checks
* Git & GitHub

---

## 📁 Project Structure

```text
two-tier-flask-app/
│
├── app.py
├── Dockerfile
├── compose.yml
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

---

## 🐳 Docker Concepts Practiced

This project helped me practice several important Docker concepts:

### 1. Docker Images

Building a custom Flask application image:

```bash
docker build -t flask-mysql-networking .
```

### 2. Docker Containers

Running the application and database as separate containers.

```bash
docker ps
```

### 3. Docker Networking

The Flask and MySQL containers communicate through a custom Docker network.

```text
Flask Container
      │
      │ Docker Network
      ▼
MySQL Container
```

The Flask application connects to MySQL using the Docker service/container name instead of `localhost`.

### 4. Docker Volumes

A named volume is used to persist MySQL data:

```yaml
volumes:
  - mysql-data:/var/lib/mysql
```

This allows database data to survive container recreation.

### 5. Health Checks

Docker health checks are used to verify that services are actually ready.

For example, MySQL can be checked using:

```yaml
healthcheck:
  test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-uroot", "-proot"]
```

### 6. Docker Compose

Docker Compose is used to manage the Flask and MySQL services together.

Start the application with:

```bash
docker compose up -d --build
```

Check the services:

```bash
docker compose ps
```

Stop the services:

```bash
docker compose down
```

---

### 7. Docker multistage build 

---

## ⚙️ Environment Configuration

The Flask application uses environment variables for database configuration.

Example:

```text
MYSQL_HOST=mysql
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=devops-mysql
```

The `mysql` hostname refers to the MySQL service inside the Docker network.

---

## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/ankit2404/two-tier-flask-app.git
```

### 2. Enter the project directory

```bash
cd two-tier-flask-app
```

### 3. Build and start the containers

```bash
docker compose up -d --build
```

### 4. Check running containers

```bash
docker compose ps
```

### 5. View logs

```bash
docker compose logs
```

For Flask:

```bash
docker compose logs flask
```

For MySQL:

```bash
docker compose logs mysql
```

### 6. Stop the application

```bash
docker compose down
```

---

## 🔍 Useful Docker Commands

List Docker images:

```bash
docker images
```

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Inspect the Docker network:

```bash
docker network inspect fastapi-mysql
```

List Docker volumes:

```bash
docker volume ls
```

View Compose services:

```bash
docker compose ps
```

---

## 📚 What I Learned

Through this project, I practiced:

* Containerizing a Flask application
* Creating Docker images using Dockerfiles
* Running multiple containers
* Connecting containers using Docker networks
* Connecting Flask with MySQL inside Docker
* Using Docker Compose
* Managing environment variables
* Using Docker volumes for persistent data
* Creating container health checks
* Understanding service dependencies
* Building and managing Docker images
* Pushing Docker images to Docker Hub
* Managing source code with Git and GitHub

---

## 🐳 Docker Hub

Docker image:

```text
ankit2404/flask-mysql-networking
```

---

## 🎯 Purpose

This project is primarily a **hands-on learning project** created to understand Docker and DevOps fundamentals by building and managing a real multi-container application.

It demonstrates how an application and database can be packaged, connected, and managed using Docker.

---

## 👨‍💻 Author

**Ankit Singh**

B.Tech Computer Science Engineering
Poornima University, Jaipur

GitHub:
https://github.com/ankit2404

---

## 📄 License & Attribution

This project was developed for educational purposes. The implementation was studied from an existing public project, and modifications were made while learning and experimenting with Docker and Flask.

Please refer to the original project's license and attribution requirements when using or redistributing related code.
