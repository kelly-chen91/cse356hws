# Use an official Python runtime as a base image
FROM python:3

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install system dependencies for MariaDB and other libraries
RUN apt update -y
RUN apt install libmariadb3 libmariadb-dev -y

# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app into the container
COPY app.py .

# Expose the port the app will run on (default is 80, can be changed if needed)
EXPOSE 80

# Run the Flask app with Gunicorn (4 workers and bind to 0.0.0.0 on port 80)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]
