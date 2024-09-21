# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV MODEL_PATH=/app/src/model/model.h5
ENV DATA_PATH=/app/data/processed/
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "src/app.py"]
