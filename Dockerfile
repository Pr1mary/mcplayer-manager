# Use Alpine as base image
FROM python:3.10-alpine AS base

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apk add --no-cache \
    mariadb-dev \
    gcc \
    python3-dev \
    musl-dev \
    libffi-dev

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# for development build
FROM base AS dev
ENV MODE=dev
ENV DB_NAME=redstonestart
ENV APP_URL=redstonestart.mraflis.com


# for production build
FROM base AS prod
ENV MODE=prod
ENV DB_NAME=redstonestart
ENV ALLOWED_HOST_LIST=mraflis.com,redstonestart.mraflis.com,192.168.1.65
ENV APP_URL=redstonestart.mraflis.com

