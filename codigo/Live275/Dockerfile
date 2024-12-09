FROM ubuntu:latest

ARG PYVERSION
ARG PYTHON_CONFIGURE_OPTS
ENV PYTHON_CONFIGURE_OPTS=$PYTHON_CONFIGURE_OPTS
ENV PYVERSION=$PYVERSION

WORKDIR /
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        git \
	lsb-release \
	software-properties-common \
	gnupg

RUN wget https://apt.llvm.org/llvm.sh
RUN chmod +x llvm.sh
RUN ./llvm.sh 18

RUN git clone https://github.com/pyenv/pyenv.git /pyenv
ENV PYENV_ROOT /pyenv
RUN eval "$(/pyenv/bin/pyenv init -)"
RUN /pyenv/bin/pyenv install $PYVERSION
RUN /pyenv/bin/pyenv global $PYVERSION

COPY nilo.py .

CMD /pyenv/versions/$PYVERSION/bin/python nilo.py