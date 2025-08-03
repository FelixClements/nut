FROM python:3.9

ARG APP_USER=nut
ARG APP_UID=1000
ARG APP_GID=1000

RUN apt-get update && apt-get install -y libusb-1.0-0-dev python3-pyqt5 libssl-dev libcurl4-openssl-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

# Create the application group and user with specified UID/GID
 RUN addgroup --gid $APP_GID $APP_USER && \
     adduser --uid $APP_UID --ingroup $APP_USER --home /home/$APP_USER --shell /bin/sh --disabled-password --gecos "" $APP_USER

# Ensure the /app directory is owned by the new user
RUN chown -R $APP_USER:$APP_USER /app

# Switch to the non-root user
USER $APP_USER

VOLUME /data

CMD ["python", "/app/nut_server.py"]
