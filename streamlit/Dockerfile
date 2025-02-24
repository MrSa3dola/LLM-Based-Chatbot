# streamlit/Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copy the frontend requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Streamlit app code into the container
COPY . .

# Expose Streamlit’s default port (8501)
EXPOSE 8501

# Run the Streamlit app with CORS disabled for simplicity
CMD ["streamlit", "run", "streamlit_app.py", "--server.enableCORS", "false"]
