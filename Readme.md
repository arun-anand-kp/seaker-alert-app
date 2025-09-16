# Seaker-Alert-App

## Overview
Seaker-Alert-App collects system metrics (CPU, RAM, Disk, Uptime, Temperature) and exposes them to Prometheus. Grafana visualizes metrics and Prometheus/Alertmanager handle alerts.
Output Screenshots are attached in (Screenshot-folder) 

## Quick start (local)
Requirements: Docker, Docker Compose
1. git clone https://github.com/arun-anand-kp/seaker-alert-app.git
2. cd Seaker-Alert-App
3. docker-compose up --
4. Grafana: http://localhost:4000 (admin/admin)
5. Prometheus: http://localhost:9090
6. Alertmanager: http://localhost:9093