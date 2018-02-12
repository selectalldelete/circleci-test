FROM python:3.5
COPY app.py test_app.py requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]