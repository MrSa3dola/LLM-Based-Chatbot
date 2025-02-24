FROM python:3.12-slim

WORKDIR /app

# Copy everything from the current directory (backend) into /app
COPY . .

# Install dependencies (assumes requirements.txt is here)
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Run the FastAPI app; note we reference main:app because main.py is at /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
