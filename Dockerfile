FROM python:3-alpine
WORKDIR /usr/src/app
EXPOSE 5000
COPY requirements.txt .
RUN pip install -qr requirements.txt
COPY . /
CMD ["python3", "./myapp.py"]
