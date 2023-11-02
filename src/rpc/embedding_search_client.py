import pickle
import uuid
import grpc
from .client import Client
from .generated import embedding_search_pb2, embedding_search_pb2_grpc


class EmbeddingSearchClient(Client):
    def __init__(self, server_address: str):
        assert type(server_address) == str

        super().__init__(server_address=server_address)

    def add_event(self, collection_name: str, embedding_id: uuid.UUID, embedding_vector: list) -> None:
        assert type(collection_name) == str
        assert type(embedding_id) == uuid.UUID
        assert type(embedding_vector) == list

        with grpc.insecure_channel(self.server_address, options=super().OPTIONS) as channel:
            stub = embedding_search_pb2_grpc.EmbeddingSearchStub(channel)

            request = embedding_search_pb2.AddEmbeddingRequest(
                collection_name=collection_name,
                embedding_id=pickle.dumps(embedding_id),
                embedding_vector=pickle.dumps(embedding_vector)
            )

            reply = stub.add_embedding(request)

            return

    def update_embedding(self, collection_name: str, embedding_id: uuid.UUID, embedding_vector: list) -> None:
        assert type(collection_name) == str
        assert type(embedding_id) == uuid.UUID
        assert type(embedding_vector) == list

        with grpc.insecure_channel(self.server_address, options=super().OPTIONS) as channel:
            stub = embedding_search_pb2_grpc.EmbeddingSearchStub(channel)

            request = embedding_search_pb2.UpdateEmbeddingRequest(
                collection_name=collection_name,
                embedding_id=pickle.dumps(embedding_id),
                embedding_vector=pickle.dumps(embedding_vector)
            )

            reply = stub.update_embedding(request)

            return

    def delete_embedding(self, collection_name: str, embedding_id: uuid.UUID) -> None:
        assert type(collection_name) == str
        assert type(embedding_id) == uuid.UUID

        with grpc.insecure_channel(self.server_address, options=super().OPTIONS) as channel:
            stub = embedding_search_pb2_grpc.EmbeddingSearchStub(channel)

            request = embedding_search_pb2.DeleteEmbeddingRequest(
                collection_name=collection_name,
                embedding_id=pickle.dumps(embedding_id)
            )

            reply = stub.delete_embedding(request)

            return

    def get_event(self, collection_name: str, embedding_vector: list, top_nearest_embedding: int) -> dict:
        assert type(collection_name) == str
        assert type(embedding_vector) == list
        assert type(top_nearest_embedding) == int

        with grpc.insecure_channel(self.server_address, options=super().OPTIONS) as channel:
            stub = embedding_search_pb2_grpc.EmbeddingSearchStub(channel)

            request = embedding_search_pb2.SearchEmbeddingRequest(
                collection_name=collection_name,
                embedding_vector=pickle.dumps(embedding_vector),
                top_nearest_embedding=top_nearest_embedding
            )

            reply = stub.search_embedding(request)

            nearest_embeddings = pickle.loads(reply.nearest_embeddings)

            return nearest_embeddings
