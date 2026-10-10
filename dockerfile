FROM python:3.12-slim
ENV ENV_APP=production
WORKDIR /app
COPY src/app.py .
COPY requirement.txt  .
RUN pip install --no-cache-dir -r requirement.txt
 CMD ["python","app.py"]