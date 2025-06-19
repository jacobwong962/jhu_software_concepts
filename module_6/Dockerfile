FROM python:3.10
COPY run.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "run.py"]