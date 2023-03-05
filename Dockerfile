FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient
COPY ./server.py /server.py
COPY ./accueil.py /accueil.py
COPY ./navbar.py /navbar.py
COPY ./album.py /album.py
COPY ./artist.py /artist.py
COPY ./employee.py /employee.py
COPY ./customer.py /customer.py
COPY ./invoice.py /invoice.py
COPY ./genre.py /genre.py
COPY ./invoiceLine.py /invoiceLine.py
COPY ./playlist.py /playlist.py
COPY ./mediatype.py /mediatype.py
COPY ./footer.py /footer.py

CMD [ "python", "/server.py", "/navbar.py", "/album.py", "/artist.py", "/employee.py", "/customer.py", "/invoice.py","/genre.py", "/invoiceLine.py", "/playlist.py","/mediatype.py","/footer.py" ]

