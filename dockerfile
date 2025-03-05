# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Ensure static files are present
RUN mkdir -p /app/static && cp static/image.jpg /app/static/

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
