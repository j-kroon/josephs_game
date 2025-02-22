# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files first to leverage Docker's layer caching
COPY pyproject.toml poetry.lock ./

# Install the dependencies using Poetry
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["poetry", "run", "python", "main.py"]
