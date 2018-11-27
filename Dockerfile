FROM ubuntu:bionic

RUN apt-get update -y \
    && apt-get dist-upgrade -y

RUN apt-get install -y automake build-essential git-core libffi-dev \
       libgmp-dev libssl-dev libtool pkg-config python3-pip python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY main.py Ginna/main.py
COPY token.txt Ginna/token.txt
COPY handlers.py Ginna/handlers.py
COPY tools.py Ginna/tools.py
COPY jobs.py Ginna/jobs.py
COPY requirements.txt Ginna/requirements.txt

RUN cd Ginna \
	&& python3 -V \
    && pip3 install --upgrade -r requirements.txt \
    && python3 main.py

WORKDIR /Ginna

ENTRYPOINT ["Ginna"]
# test ssh key