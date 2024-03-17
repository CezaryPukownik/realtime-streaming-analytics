# Kafka-ClickHouse Integration POC with Graphana

This project sets up a Proof of Concept (POC) on a local machine for real-time event streaming and analytics using Kafka, ClickHouse, and Graphana, all containerized and managed via Docker.

## Components:

- **Zookeeper**: A centralized service for maintaining configuration information, naming, and providing distributed synchronization.
- **Kafka**: A distributed streaming platform for handling real-time data feeds.
- **ClickHouse**: An open-source, column-oriented database management system for online analytical processing.
- **Graphana**: An open-source business intelligence tool that allows you to query and visualize data.
- **Producer**: A Python service that generates and sends messages to Kafka.
- **Consumer**: A Python service that consumes messages from Kafka and stores them in ClickHouse.

## Quick Start Guide

### Prerequisites:
- Docker
- Docker-Compose
- Git (optional, for cloning the repository)

### Steps to run the application:

1. Clone the repository or download the source code:

```bash
git clone https://github.com/CezaryPukownik/realtime-streaming-analytics
cd realtime-streaming-analytic
```
   
2. Build and start the services using Docker Compose:
   
```bash
docker-compose up -d --build
```

   
3. Visit http://localhost:3000 to access the Graphana interface and configure it to connect to the ClickHouse database.
4. Run the Kafka producer to send messages to the Kafka broker:
   The producer is already set up as a Docker service and will begin sending messages once the stack is up.
5. Use the Graphana UI to create queries and dashboards to visualize the data stored in ClickHouse.
6. To stop and remove all running services, execute:
   
```bash
docker-compose down
```
   
This POC is configured to run without additional environment setup and should work on any system that supports Docker. After starting the application, you can modify the producer and consumer scripts to customize data generation and consumption according to your needs.