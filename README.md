# Observability Stack

Centralized monitoring and alerting platform.

## Features
- **Metrics**: Prometheus scraping from multiple services.
- **Dashboards**: Grafana pre-provisioned with Prometheus datasource.
- **Logging**: Logstash consuming from Kafka, indexing into Elasticsearch.
- **Anomaly Detection**: Python service detecting latency spikes using Z-score logic.

## Stack
- **Prometheus**: Metric collection.
- **Grafana**: Visualization.
- **ELK (Partial)**: Logstash + Elasticsearch.
- **Python**: Anomaly detection logic.

## Setup
```bash
docker-compose up --build
```
- Grafana: `http://localhost:3000` (admin/admin)
- Prometheus: `http://localhost:9090`
- Elasticsearch: `http://localhost:9200`
