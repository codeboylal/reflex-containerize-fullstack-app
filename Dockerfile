# Use the official Python image from DockerHub
FROM python:3.12-slim

# Install curl and any other required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Install Reflex CLI
RUN pip install reflex-cli

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file to install dependencies
COPY requirements.txt .

# Install the necessary Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app to the working directory in the container
COPY . .

# Run migrations for the database
RUN reflex db migrate

# Expose the default port for the app
EXPOSE 3000
EXPOSE 8000


# Command to run the Reflex app
CMD ["reflex", "run"]






