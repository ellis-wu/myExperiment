FROM ubuntu:14.04
MAINTAINER elliswu<ellis.w@inwinstack.com>

RUN apt-get update && apt-get install -y apache2 php5 libapache2-mod-php5 php5-mcrypt && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY stress.php /var/www/html/
COPY load.php /var/www/html/
WORKDIR test-code
COPY run.sh run.sh
RUN chown root.root run.sh && chmod 700 run.sh

EXPOSE 80

ENTRYPOINT ["/test-code/run.sh"]

