FROM ubuntu:16.04
 RUN apt-get update && \
      apt-get install -y python-minimal python-pip python-setuptools --no-install-recommends && \
     apt-get clean && \ 
     rm -rf /var/lib/apt/lists/*                                     
ENV FLASK_APP=app.py
WORKDIR /usr/src
COPY . /usr/src
RUN pip install -r requirements.txt
CMD ["flask","run"] 
