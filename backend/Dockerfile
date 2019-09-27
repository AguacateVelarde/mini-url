FROM python:3.6.2
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN chmod 777 /usr/src/app/entrypoint.sh
RUN pip install --no-cache-dir -r requirements.txt
COPY ./uwsgi.ini /etc/uwsgi.ini
EXPOSE 5000

CMD ["python", "app.py"]