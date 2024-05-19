# Use an official Python runtime as a parent image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR .

# Copy the current directory contents into the container at /usr/src/app
COPY . .
ENV PYTHONUNBUFFERED=1



COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt
CMD ["python3", "app.py"]