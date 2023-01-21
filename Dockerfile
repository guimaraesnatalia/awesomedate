FROM python:3.9
ADD ./main.py .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "./main.py"]