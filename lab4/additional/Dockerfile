FROM p4lang/p4c@sha256:f13043e74216d0b50e2a6d24624d2b393ee1ec0a6575587ec47277df6c8deebf
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    make sudo mininet iproute2 iputils-ping net-tools ethtool tcpdump \
    python3-pip python3-venv python3-scapy python3-pexpect \
    libboost-iostreams-dev libboost-graph-dev \
    && rm -rf /var/lib/apt/lists/*
ENV PYTHONPATH=/usr/local/lib/python3.12/site-packages:/usr/local/lib/python3.12/dist-packages
RUN python3 -m pip install --break-system-packages protobuf==3.20.3 grpcio googleapis-common-protos scapy ptf
RUN python3 -c "import site,pathlib; pathlib.Path(site.getsitepackages()[0], 'mininet-system.pth').write_text('/usr/lib/python3/dist-packages\n')"
WORKDIR /work
