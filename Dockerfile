FROM python:3.8-slim-buster

WORKDIR /app

COPY search_pi/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY search_pi/ .

# Environment Variables
ENV FLASK_APP=findPath.py
ENV FLASK_ENV=production

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--no-debugger"]
EXPOSE 5000