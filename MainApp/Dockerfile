FROM python:3.10.4

WORKDIR /usr/src/kota-hr

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

CMD ["python3", "./Services/main.py"]