import random


def longest_linked_list_chain(keys, buckets, loops=10):
    for i in range(loops):
        key_counts = {}
        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1
        # tally up and find the largest linked list chain (index where we had most collision)
        largest_number = 0
        for key in key_counts:
            if key_counts[key] > largest_number:
                largest_number = key_counts[key]

        print(f'Longest linked list chain for {keys} keys in {buckets} buckets /'
              f'(Load Factor: {keys/buckets:.2f}:{largest_number})')

longest_linked_list_chain(3, 5, 10)