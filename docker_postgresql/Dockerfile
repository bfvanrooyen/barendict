FROM ubuntu:14.04
MAINTAINER Barend Fouché van Rooyen
EXPOSE 5432

#set locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get upgrade -y && apt-get install postgresql-9.3 -y;

USER postgres

RUN service postgresql start &&\
psql --command "CREATE USER barendict WITH SUPERUSER PASSWORD 'barendict';" &&\
createdb -O barendict barendict ;\
echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf &&\
echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf && \
service postgresql stop

VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

CMD ["/usr/lib/postgresql/9.3/bin/postgres", "--config-file=/etc/postgresql/9.3/main/postgresql.conf"]
