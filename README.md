# Observability Stack
Centralized monitoring and alerting platform.

## Overview
A telemetry stack for metrics, logs, and anomaly detection across distributed services.

## Components
- Prometheus: Scrapes metrics from microservices.
- Grafana: Data visualization with pre-provisioned dashboards.
- ELK Stack (Partial): Logstash for log ingestion and Elasticsearch for indexing.
- Anomaly Detector: Python service for latency spike detection using Z-score algorithms.

## Features
- Alerting Rules: Pre-configured rules for latency (P95) and service downtime.
- Log Aggregation: Centralized logging for Kafka events.
- Anomaly Detection: Automated traffic pattern analysis.

## Setup
1. Start services:
   ```bash
   docker-compose up --build -d
   ```
2. Access:
   - Grafana: `http://localhost:3000` (admin/admin)
   - Prometheus: `http://localhost:9090`
   - Elasticsearch: `http://localhost:9200`
