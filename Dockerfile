# Use official Python image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV USE_GPU=false
# Use a custom temp directory for pip unpacking to avoid /tmp filling up
ENV TMPDIR=/app/tmp
RUN mkdir -p /app/tmp

# Set working directory
WORKDIR /app

# Combine system installs and clean up apt cache in one layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /app/tmp

COPY requirements.txt /app/

# Combined RUN for smaller image footprint
RUN if [ "$USE_GPU" = "true" ]; then \
    pip install --no-cache-dir -r requirements.txt; \
    else \
    pip install --no-cache-dir -r requirements.txt; \
    fi && rm -rf /app/tmp/*
    
# Copy project files
COPY . .

# Expose port and run server
EXPOSE 8000

# Start the Django development server

CMD ["python", "airline/manage.py", "runserver", "0.0.0.0:8000"]
# End of Dockerfile
