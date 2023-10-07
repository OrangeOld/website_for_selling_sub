FROM python:latest

ENTRYPOINT ["top", "-b"]

WORKDIR /usr/src/website_for_selling_sub

COPY ./req /usr/src/req

RUN pip install -r /usr/src/req

COPY . /usr/src/website_for_selling_sub

CMD ["python","manage.py","runserver","127.0.0.1:9000"]
