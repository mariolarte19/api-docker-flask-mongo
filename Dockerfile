FROM python:3.9.6 
WORKDIR /api
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt /api
RUN pip install -r requirements.txt
EXPOSE 5000
COPY app.py /api
CMD ["python", "app.py"]