from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddEmbeddingReplay(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AddEmbeddingRequest(_message.Message):
    __slots__ = ["collection_name", "embedding_id", "embedding_vector"]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_ID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_VECTOR_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embedding_id: bytes
    embedding_vector: bytes
    def __init__(self, collection_name: _Optional[str] = ..., embedding_id: _Optional[bytes] = ..., embedding_vector: _Optional[bytes] = ...) -> None: ...

class DeleteEmbeddingReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteEmbeddingRequest(_message.Message):
    __slots__ = ["collection_name", "embedding_id"]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_ID_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embedding_id: bytes
    def __init__(self, collection_name: _Optional[str] = ..., embedding_id: _Optional[bytes] = ...) -> None: ...

class SearchEmbeddingReply(_message.Message):
    __slots__ = ["nearest_embeddings"]
    NEAREST_EMBEDDINGS_FIELD_NUMBER: _ClassVar[int]
    nearest_embeddings: bytes
    def __init__(self, nearest_embeddings: _Optional[bytes] = ...) -> None: ...

class SearchEmbeddingRequest(_message.Message):
    __slots__ = ["collection_name", "embedding_vector", "top_nearest_embedding"]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_VECTOR_FIELD_NUMBER: _ClassVar[int]
    TOP_NEAREST_EMBEDDING_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embedding_vector: bytes
    top_nearest_embedding: int
    def __init__(self, collection_name: _Optional[str] = ..., embedding_vector: _Optional[bytes] = ..., top_nearest_embedding: _Optional[int] = ...) -> None: ...

class UpdateEmbeddingReply(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateEmbeddingRequest(_message.Message):
    __slots__ = ["collection_name", "embedding_id", "embedding_vector"]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_ID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_VECTOR_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embedding_id: bytes
    embedding_vector: bytes
    def __init__(self, collection_name: _Optional[str] = ..., embedding_id: _Optional[bytes] = ..., embedding_vector: _Optional[bytes] = ...) -> None: ...
