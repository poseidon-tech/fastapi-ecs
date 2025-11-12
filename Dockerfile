FROM python:3.11-slim

WORKDIR /app

# Install FastAPI and Uvicorn directly
RUN pip install --no-cache-dir fastapi[standard]

# Copy your FastAPI code
COPY . .

EXPOSE 8000

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
