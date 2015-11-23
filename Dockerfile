FROM ubuntu:trusty
MAINTAINER Richard Panek <thatinstant@gmail.com>

# Get and install required packages.
RUN apt-get update && apt-get install -y -q \
    build-essential \
    libjansson-dev \
    libpcre3-dev \
    libssl-dev \
    libxml2-dev \
    zlib1g-dev \
    python-dev \
    python-pip \
  && rm -rf /var/lib/apt/lists/*

# Create a place to deploy the application
ENV APP_DIR /var/www/app
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

COPY ./leo_web $APP_DIR/
RUN pip install -r $APP_DIR/requirements.txt
COPY ./run.sh $APP_DIR/
RUN chmod +x $APP_DIR/run.sh
EXPOSE 9000 9002
CMD ["/var/www/app/run.sh"]
