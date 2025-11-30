# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that ADK Web runs on
EXPOSE 8080

# Define environment variable for ADK to bind to all interfaces
ENV HOST=0.0.0.0
ENV PORT=8080

# Run adk web when the container launches
# We use the port provided by the environment (Render sets $PORT)
CMD ["sh", "-c", "adk web . --port $PORT --host 0.0.0.0"]
