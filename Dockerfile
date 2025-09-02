FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy requirements
COPY ./requirements.txt .



RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt 

RUN /py/bin/python -m spacy download en_core_web_sm


# Copy project files
COPY . .

EXPOSE 8000 

#set path
ENV PATH="/py/bin:$PATH"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
