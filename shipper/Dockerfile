FROM python:3.9

COPY ./requirements.txt /.
RUN pip install -r ./requirements.txt

COPY . /opt/shipper
WORKDIR /opt/shipper

CMD ["python", "shipper.py"]