FROM python:3.10.6-slim

RUN mkdir "my-code"
WORKDIR /my-code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python","location_writer.py"]
