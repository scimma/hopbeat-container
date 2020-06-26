###
### Author: rdt12@psu.edu
### Date:   Jun 26, 2020
### Desc:   Build a container that sends a heartbeat message every 30 seconds
###         using the hop library.
###
FROM scimma/base:0.1.1
RUN  mkdir -p /usr/local/src
RUN yum -y install git unzip
RUN cd /usr/local/src && \
    curl -s "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws
ADD scripts/hopBeat /root/hopBeat
ADD scripts/Utils.py       /root/Utils.py
ADD scripts/runHopBeat.py /root/runHopBeat.py
RUN chmod ugo+rx /root/hopBeat
RUN chmod ugo+rx /root/runHopBeat.py
WORKDIR /tmp
ENTRYPOINT ["/root/runHopBeat.py"]
