# Use official Python image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set GPU environment variable
ENV USE_GPU=false

# Install Python dependencies
COPY requirements.txt /app/
RUN if [ "${USE_GPU}" = "true" ]; then \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --break-system-packages -r requirements.txt; \
else \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --break-system-packages -r requirements.txt; \
fi && rm -rf /root/.cache/pip /tmp/*

# Copy project files
COPY . .

# Expose Django port
EXPOSE 8000

# Run Django server
CMD ["python", "airline/manage.py", "runserver", "0.0.0.0:8000"]

#run on http://localhost:8000


