# Use lightweight Python
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose dashboard
EXPOSE 8000

# Run bot
CMD ["python3", "main.py"]
