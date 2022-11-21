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
    python3.10 \
    telnet \
    telnetd \
    netcat \
    dnsutils \
    curl

# Create the "uwe" user account
RUN useradd -m -s /bin/bash -p "$(openssl passwd -1 uwe)" uwe 
