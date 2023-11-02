import config
from embedding_search_service import EmbeddingSearchService


def main():
    service = None

    try:
        print('Starting embedding search service...')

        service = EmbeddingSearchService(
            address=config.EMBEDDING_SEARCH_SERVICE_BINDING_ADDRESS,
            max_workers=config.EMBEDDING_SEARCH_SERVICE_MAX_WORKERS
        )

        service.start()

        service.wait_for_termination()

    finally:
        if service is not None:
            service.stop()

        print('Search service stopped.')


if __name__ == '__main__':
    main()
