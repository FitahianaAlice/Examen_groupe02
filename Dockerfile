FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient
COPY ./server.py /server.py
COPY ./navbar.py /navbar.py
COPY ./album.py /album.py
COPY ./artist.py /artist.py
CMD [ "python", "/server.py", "/navbar.py", "/album.py", "/artist.py" ]
