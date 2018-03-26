FROM jazzdd/alpine-flask

ENV FLASK_APP=/app/app.py

RUN mkdir /app/templates && mkdir ~/.aws && mkdir /app/plugins
COPY ["requirements.txt", "/"]
COPY ["./webapp/app.py", "/app/"]
COPY ["./webapp/templates/*", "/app/templates/"]
COPY ["./webapp/plugins/*", "/app/plugins/"]
COPY ["setup-access.sh", "/tmp/"]
RUN chmod +x /tmp/setup-access.sh
RUN echo '/tmp/setup-access.sh' >> /entrypoint.sh
RUN pip install -r /requirements.txt
ENTRYPOINT ["/tmp/setup-access.sh"]
