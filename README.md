# mediawall-vss-dispatcher

A VSS (Video Streaming Service) dispatcher service.

## Project Structure

```
mediawall-vss-dispatcher/
├─ src/
│  ├─ main.py
│  ├─ dispatcher/
│  │  ├─ __init__.py
│  │  └─ logic.py
├─ requirements.txt
├─ Dockerfile
├─ README.md
└─ .github/
   └─ workflows/
      └─ deploy.yml
```

## Configuration

The service reads configuration from the following paths:

- `/config/broker/rabbitmq.yaml` - RabbitMQ broker configuration
- `/config/vss/vss.yaml` - VSS configuration
- `/config/services/global.yaml` - Global service configuration

## Running the Service

### Local Development

```bash
pip install -r requirements.txt
python src/main.py
```

### Docker

```bash
docker build -t mediawall-vss-dispatcher .
docker run mediawall-vss-dispatcher
```