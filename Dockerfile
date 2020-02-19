FROM python:3.6
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY scope.yml /app/scope.yml
RUN pip install -r requirements.txt
COPY . /app
CMD ["scope-run", "gunicorn", "restaurants.wsgi:application", "-b", "0.0.0.0:8000"]
