FROM python:3.12-alpine3.20

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src src

EXPOSE 7000

HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 CMD curl --fail http://localhost:7000/health || exit 1

ENTRYPOINT ["python", "./src/app.py"]
