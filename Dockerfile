# Use the official Ubuntu base image
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Update the package list and install Tesseract OCR
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev django pillow

# Copy your application files into the container (if needed)
COPY . /app

# Specify the default command to run when the container starts
CMD ["bash"]
