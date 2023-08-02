# Use the official Python 3.8 slim-buster image as the base image.
# This will provide a minimal Debian-based environment with Python 3.8 installed.
FROM python:3.8-slim-buster

# Set the working directory inside the container to '/app'.
WORKDIR /app

# Copy the 'requirements.txt' file from the host to the container's '/app' directory.
COPY requirements.txt requirements.txt

# Copy the 'db' folder from the host to the container's '/app/db' directory.
# This folder contains the necessary SQL files for the application.
COPY app/db/ db

# Install the Python dependencies listed in 'requirements.txt'
# using pip3 within the container.
RUN pip3 install -r requirements.txt

# Copy all the files and folders from the host to the container's '/app' directory.
COPY . .

# Set the default command to run when the container starts.
# It runs two Python scripts in the background using '&':
# - data_generator.py to generate data (Note: '-u' is used for unbuffered output)
# - main.py to start the main application (Note: '-u' is used for unbuffered output)
CMD python -u app/data_generator.py & python -u app/main.py
