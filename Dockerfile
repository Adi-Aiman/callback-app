

#docker build -t flask-gunicorn-app .
#docker run --name my_flask -p 8000:8000 flask-gunicorn-app
# add -d to run as daemon an use
#docker logs <container_id> for logs
FROM python:3.12-slim

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV GIT_TOKEN=""

# Create the startup script inside the image
RUN echo '#!/bin/sh\n\
echo "Cloning repo..."\n\
git clone https://github.com/Adi-Aiman/callback-app.git /app\n\
cd /app\n\
echo "Installing dependencies..."\n\
pip install --no-cache-dir -r requirements.txt\n\
echo "Starting app..."\n\
gunicorn --bind 0.0.0.0:80 app:app' > /start.sh && chmod +x /start.sh

EXPOSE 80

CMD ["/start.sh"]

