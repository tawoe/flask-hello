FROM python:3.11.1-slim
COPY app.py app/
COPY requirements.txt app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
USER 1001
ENTRYPOINT ["python3", "app.py"]