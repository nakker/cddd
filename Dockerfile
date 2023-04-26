FROM tensorflow/tensorflow:1.15.5-gpu-py3
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN  apt-get install python-rdkit librdkit1 rdkit-data
RUN pip install scikit-learn
COPY . ./

RUN pip install .
