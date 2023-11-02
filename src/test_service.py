import uuid
import numpy as np
import rpc

EMBEDDING_SEARCH_SERVICE_ADDRESS = 'localhost:14805'
collection_name = 'test_collection'
top_number = 2


def add_embedding():
    client = rpc.EmbeddingSearchClient(EMBEDDING_SEARCH_SERVICE_ADDRESS)
    uuid_list = []
    for i in range(10):
        rand_vec = np.random.rand(10).tolist()
        idx = uuid.uuid4()
        uuid_list.append(idx)
        client.add_embedding(collection_name, idx, rand_vec)
    return uuid_list


def update_embedding(uuid_list):
    client = rpc.EmbeddingSearchClient(EMBEDDING_SEARCH_SERVICE_ADDRESS)

    index = int(input('please inter embedding id between 0 to 9 :'))
    idx = uuid_list[index]
    rand_vec = np.random.rand(10).tolist()
    client.update_embedding(collection_name, idx, rand_vec)


def delete_embedding(uuid_list):
    client = rpc.EmbeddingSearchClient(EMBEDDING_SEARCH_SERVICE_ADDRESS)
    index = int(input('please inter embedding id between 0 to 9 :'))
    idx = uuid_list[index]
    client.delete_embedding(collection_name, idx)


def search_embedding():
    client = rpc.EmbeddingSearchClient(EMBEDDING_SEARCH_SERVICE_ADDRESS)
    rand_vec = np.random.rand(10).tolist()
    top_nearest_neighbor = client.search_embedding(collection_name, rand_vec, top_number)
    print(top_nearest_neighbor)


def main():
    while True:
        print('Events service address: {}'.format(EMBEDDING_SEARCH_SERVICE_ADDRESS))
        print()

        print('Menu:')
        print('0) exit')
        print('1) update_embedding')
        print('2) delete_embedding')
        print('3) search_embedding')
        print()

        choice = int(input('Press enter your choice: '))
        print()

        print('--------------------------------------------------------------------------------')
        print()
        id_list = add_embedding()
        if choice == 0:
            break

        if choice == 1:
            update_embedding(id_list)
        if choice == 2:
            delete_embedding(id_list)
        if choice == 3:
            search_embedding()

        print('################################################################################')
        print()


if __name__ == '__main__':
    main()
