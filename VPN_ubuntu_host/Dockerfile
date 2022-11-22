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
    curl \
    tcpdump

COPY get-pip.py /tmp

RUN  python3 /tmp/get-pip.py \
     && pip3 install scapy \
     && rm /tmp/get-pip.py

RUN useradd -ms /bin/bash -p "$(openssl passwd -1 uwe)" uwe
