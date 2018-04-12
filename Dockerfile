FROM ubuntu:16.04
 RUN apt-get update && \
      apt-get install -y python-minimal python-pip python-setuptools --no-install-recommends && \
     apt-get clean && \ 
     rm -rf /var/lib/apt/lists/*                                     
ENV FLASK_APP=app.py
WORKDIR /usr/src
COPY . /usr/src
RUN pip install -r requirements.txt
EXPOSE 5000
HEALTHCHECK --timeout=3s CMD curl -f http://localhost:5000/ || exit1
CMD ["flask","run", "-h","0.0.0.0"] 
