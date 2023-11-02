import uuid
from qdrant_client import models
from qdrant_client import QdrantClient
import config
import rpc


class EmbeddingSearchService(rpc.EmbeddingSearchServer):
    def __init__(self, address, max_workers):
        super().__init__(address, max_workers)

        self._qdrant_db_client = None
        self._initialized = False
        self._collection_names = None

    def start(self):
        self._initialize()
        self._get_collection_names()
        super().start()

    def stop(self):
        super().stop()
        self._release()

    def on_add_embedding(self, collection_name: str, embedding_id: uuid.UUID, embedding_vector: list[int]) -> None:

        if collection_name not in self._collection_names:
            self._create_collection(collection_name, len(embedding_vector))

        self._qdrant_db_client.upsert(collection_name=collection_name,
                                      points=[
                                          models.PointStruct(
                                              id=str(embedding_id),
                                              vector=embedding_vector
                                          )
                                      ]
                                      )

    def on_update_embedding(self, collection_name: str, embedding_id: uuid.UUID, embedding_vector: list[int]) -> None:

        if collection_name not in self._collection_names:
            raise Exception(f'Collection {collection_name} not exist')

        self._qdrant_db_client.update_vectors(
            collection_name=collection_name,
            vectors=[
                models.PointStruct(
                    id=str(embedding_id),
                    vector=embedding_vector
                )
            ]
        )

    def on_delete_embedding(self, collection_name: str, embedding_id: uuid.UUID) -> None:

        if collection_name not in self._collection_names:
            raise Exception(f'Collection {collection_name} not exist')

        self._qdrant_db_client.delete(
            collection_name=collection_name,
            points_selector=models.PointIdsList(
                points=[str(embedding_id)],
            ),
        )

    def on_search_embedding(self, collection_name: str, embedding_vector: list, top_nearest_embedding: int) -> list[
        uuid.UUID]:

        if collection_name not in self._collection_names:
            raise Exception(f'Collection {collection_name} not exist')

        event_ids = self._qdrant_db_client.search(
            collection_name=collection_name,
            query_vector=embedding_vector,
            limit=top_nearest_embedding
        )

        return [uuid.UUID(point.id) for point in event_ids]

    def _initialize(self):
        if self._initialized:
            raise Exception('The object already is initialized.')

        self._qdrant_db_client = QdrantClient(host=config.QDRANT_STORAGE_IP,
                                              port=config.QDRANT_STORAGE_PORT)

        self._initialized = True

    def _release(self):
        if self._initialized:
            if self._qdrant_db_client is not None:
                self._qdrant_db_client = None
            if self._collection_names is not None:
                self._collection_names = None

        self._initialized = False

    def _get_collection_names(self):
        if self._qdrant_db_client is not None:
            collection_names_list = [collection_info['name'] for collection_info in
                                     self._qdrant_db_client.get_collections().dict()['collections']]
            if len(collection_names_list):
                self._collection_names = collection_names_list
        return None

    def _create_collection(self, collection_name, embedding_size):

        self._qdrant_db_client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=embedding_size,
                                               distance=models.Distance.COSINE,
                                               on_disk=config.WRITE_ON_DISK),
            optimizers_config=models.OptimizersConfigDiff(memmap_threshold=config.MEMORY_MAP_THRESHOLD)
        )
