FROM python:3.9-slim
WORKDIR /app
COPY main.py .
ENV PORT 8000
EXPOSE $PORT
CMD ["python", "main.py"]
