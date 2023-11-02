import os

QDRANT_STORAGE_IP = os.getenv('QDRANT_STORAGE_IP', 'localhost')
QDRANT_STORAGE_PORT = os.getenv('QDRANT_STORAGE_PORT', '6333')
QDRANT_COLLECTION_NAME = os.getenv('QDRANT_COLLECTION_NAME', 'face_embedding_collection')

MEMORY_MAP_THRESHOLD = int(os.getenv('MEMORY_MAP_THRESHOLD', 20000))
WRITE_ON_DISK = os.getenv('WRITE_ON_DISK', 'True').lower() in ['true', '1']

EMBEDDING_SEARCH_SERVICE_BINDING_ADDRESS = os.getenv('SEARCH_SERVICE_BINDING_ADDRESS', '0.0.0.0:14805')
EMBEDDING_SEARCH_SERVICE_MAX_WORKERS = int(os.getenv('SEARCH_SERVICE_MAX_WORKERS', '8'))
