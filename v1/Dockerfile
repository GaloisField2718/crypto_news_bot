FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock first for better caching
COPY Pipfile Pipfile.lock ./

# Install dependencies using pipenv
RUN pipenv install --system --deploy

# Copy the rest of the application
COPY . .

# Create logs directory
RUN mkdir -p logs

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Run the bot
CMD ["python", "main.py"] 