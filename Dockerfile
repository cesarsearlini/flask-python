FROM python:3.8-slim-buster
ENV LISTEN_PORT 5000
EXPOSE 5000
COPY . .
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app.wsgi:app"]