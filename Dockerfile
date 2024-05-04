FROM python:3.10

ADD checkout.py .
ADD models.py .
ADD tests.py .

CMD ["python", "./tests.py"]

CMD ["python", "./checkout.py"]