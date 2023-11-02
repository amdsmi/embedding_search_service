FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN \
    apt-get update && \
    apt-get install --yes \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Note: Docker context refers to the root directory of the project.

COPY ./embedding_search_service/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

COPY ./embedding_search_service/src/ ./

RUN rm ./rpc ./VERSION
COPY ./common/rpc/ ./rpc/
COPY ./VERSION ./

CMD ["python3", "main.py"]
