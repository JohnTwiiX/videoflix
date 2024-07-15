FROM python:3.12

WORKDIR /app

# Copy the directory
COPY . .

# Install required packages
RUN apt-get update && \
    apt-get install -y ffmpeg build-essential gcc netcat-openbsd dos2unix

# Convert entrypoint.sh to Unix format and ensure it's executable
RUN dos2unix /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Install requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port
EXPOSE 8060

# Start the application
ENTRYPOINT ["/app/entrypoint.sh"]
