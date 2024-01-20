# Use the official Ubuntu base image
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Update the package list and install Tesseract OCR
RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y libtesseract-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy your application files into the container (if needed)
COPY . /app

# Specify the default command to run when the container starts
CMD ["bash"] 