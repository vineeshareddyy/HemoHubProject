# Base Dockerfile for shared dependencies
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a directory for the app
WORKDIR /code

# Copy only the requirements file first to leverage Docker's caching
COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt


