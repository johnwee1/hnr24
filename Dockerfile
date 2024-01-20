# Use the official Ubuntu base image
FROM ubuntu:22.04

# Set the working directory
WORKDIR /app

# Update the package list and install Tesseract OCR
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y libtesseract-dev
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y ffmpeg libsm6 libxext6

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
# Copy your application files into the container (if needed)
COPY . /app

WORKDIR /app/backend/optical
# Specify the default command to run when the container starts
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["bash"]