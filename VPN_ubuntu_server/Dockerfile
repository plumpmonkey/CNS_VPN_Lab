FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt install -y \
    nano \
    binutils \
    iproute2 \
    iputils-ping \
    net-tools \
    iptables \
    python3 \
    telnet \
    telnetd \
    netcat \
    dnsutils \
    curl

COPY get-pip.py /tmp

RUN  python3 /tmp/get-pip.py \
     && pip3 install scapy \
     && rm /tmp/get-pip.py

COPY 99-forward.conf /etc/sysctl.d/
