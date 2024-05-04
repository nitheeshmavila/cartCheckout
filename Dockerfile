FROM python:3.10

ADD src/checkout.py .
ADD src/models.py .
ADD tests.py .

CMD ["python", "./tests.py"]

CMD ["python", "./checkout.py"]