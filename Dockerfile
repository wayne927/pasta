FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
ENV PASTA_ROOT=/var/www/pasta

RUN apt-get update
RUN apt-get -y install vim

RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install Flask
RUN pip3 install redis

RUN apt-get -y install apache2
RUN apt-get -y install libapache2-mod-wsgi-py3

RUN apt-get -y install cron

COPY 000-default.conf /etc/apache2/sites-available/

# dev mode -- mount source code from host to container
#RUN mkdir /var/www/pasta/

# prod mode -- copy source code into container and 
# turn on clean up job
COPY pasta /var/www/pasta/
RUN chmod a+w /var/www/pasta/files
RUN crontab < /var/www/pasta/cronjob.txt

#CMD ["apachectl", "-DFOREGROUND"]
CMD service cron start && apachectl -DFOREGROUND
