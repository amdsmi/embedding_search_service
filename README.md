# embedding search service

This project contains implementation of embedding search service.

## Requirements

**Python**:

```shell
$ sudo apt install python3 python3-wheel python3-pip python3-venv python3-dev python3-setuptools
```

## Virtual Environments

Create an isolated Python virtual environment using the `venv` standard library module. This will keep dependant Python
packages from interfering with other Python projects on your system.

```shell
$ python3 -m venv venv
$ source venv/bin/activate
```

Once activated, update core packaging tools (`pip`, `wheel`, and `setuptools`) to the latest versions.

```shell
(venv) $ pip install --upgrade pip wheel setuptools
```

## Install Dependencies

To update dependencies, run the following command on terminal:

```shell
(venv) $ pip install -r requirements.txt
```

## Run Service

To run service, run the following commands on terminal:

```shell
(venv) $ cd src
(venv) $ python main.py
```

## Test Service

To test service, run the following commands on terminal:

```shell
(venv) $ cd src
(venv) $ python test_service.py
```

## Compiling Protocol Buffers (`protos`)

To compile protocol buffers, run the following commands on terminal:

```shell
(venv) $ pip install grpcio-tools

(venv) $ cd src/rpc
(venv) $ python -m grpc_tools.protoc \
    --proto_path=./protos \
    --python_out=./generated \
    --pyi_out=./generated \
    --grpc_python_out=./generated \
    ./protos/storage.proto
(venv) $ sed -i -E 's/^import.*_pb2/from . \0/' ./generated/embedding_search_pb2_grpc.py
```

## Configurations

To change configurations, you can set the following environment variables (set in `src/config.py`).

| Name                                       | Default Value              |
|--------------------------------------------|----------------------------|
| `QDRANT_STORAGE_IP`                        | `'localhost'`              |
| `QDRANT_STORAGE_PORT`                      | `6333`                     |
| `QDRANT_COLLECTION_NAME`                   | `'QDRANT_COLLECTION_NAME'` |
| `MEMORY_MAP_THRESHOLD`                     | `20000`                    |
| `WRITE_ON_DISK`                            | `True`                     |
| `EMBEDDING_SEARCH_SERVICE_BINDING_ADDRESS` | `0.0.0.0:14805 `           |
| `EMBEDDING_SEARCH_SERVICE_MAX_WORKERS`     | `8`                        |
