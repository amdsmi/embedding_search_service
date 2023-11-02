import pickle
import uuid
from abc import abstractmethod
from .generated import embedding_search_pb2, embedding_search_pb2_grpc
from .server import Server


class EmbeddingSearchServer(Server):
    def __init__(self, address: str, max_workers: int):
        assert type(address) == str
        assert type(max_workers) == int

        super().__init__(
            address=address,
            max_workers=max_workers,
            add_servicer_to_server_callback=embedding_search_pb2_grpc.add_EmbeddingSearchServicer_to_server()
        )

    @abstractmethod
    def on_add_embedding(self, collection_name: str, embedding_id: uuid.UUID, embedding_vector: list) -> None:
        pass

    @abstractmethod
    def on_update_embedding(self, collection_name: str, embedding_id: uuid.UUID, embedding_vector: list) -> None:
        pass

    @abstractmethod
    def on_delete_embedding(self, collection_name: str, embedding_id: uuid.UUID) -> None:
        pass

    @abstractmethod
    def on_search_embedding(self, collection_name: str, embedding_vector: list, top_nearest_embedding: int) -> list:
        pass

    def add_embedding(self, request, context):
        collection_name = request.collection_name
        embedding_id = pickle.loads(request.embedding_id)
        embedding_vector = pickle.loads(request.embedding_vector)

        self.on_add_embedding(collection_name, embedding_id, embedding_vector)

        reply = embedding_search_pb2.AddEmbeddingReplay()

        return reply

    def update_embedding(self, request, context):
        collection_name = request.collection_name
        embedding_id = pickle.loads(request.embedding_id)
        embedding_vector = pickle.loads(request.embedding_vector)

        self.on_update_embedding(collection_name, embedding_id, embedding_vector)

        reply = embedding_search_pb2.UpdateEmbeddingReply()

        return reply

    def delete_embedding(self, request, context):
        collection_name = request.collection_name
        embedding_id = pickle.loads(request.embedding_id)

        self.on_delete_embedding(collection_name, embedding_id)

        reply = embedding_search_pb2.DeleteEmbeddingReply()

        return reply

    def search_embedding(self, request, context):
        collection_name = request.collection_name
        embedding_vector = pickle.loads(request.embedding_vector)
        top_nearest_embedding = request.top_nearest_embedding

        nearest_embeddings = self.on_search_embedding(collection_name, embedding_vector, top_nearest_embedding)
        assert type(nearest_embeddings) == list

        reply = embedding_search_pb2.SearchEmbeddingReply(
            nearest_embeddings=pickle.dumps(nearest_embeddings)
        )

        return reply
