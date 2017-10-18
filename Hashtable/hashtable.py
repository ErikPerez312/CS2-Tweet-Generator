from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table."""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:  # O(n^2) quadratic time
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table."""
        # TODO: Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:  # O(n^2) quadratic time
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table."""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:  # linear time
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets."""
        # TODO: Count number of key-value entries in each of the buckets
        count = 0
        for bucket in self.buckets:  # linear time
            count += bucket.length()
            # count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False."""
        # TODO: Check if the given key exists in a bucket
        key_hash = self._bucket_index(key)
        bucket = self.buckets[key_hash]

        key_found = bucket.find(lambda item: item[0] == key)
        if key_found:
            return True
        return False
        # if self.buckets[key_hash] is not None:  # constant
        #     bucket = self.buckets[key_hash]
        #     if not bucket.is_empty() and bucket.head.data[0] == key:
        #         return True
        #     return False
        # update with get body

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError."""
        # TODO: Check if the given key exists and return its associated value
        # current_node = bucket.head
        # while current_node is not None:  # Linear time
        #     if current_node.data[0] == key:  # Constant
        #         return current_node.data[1]

        key_hash = self._bucket_index(key)
        bucket = self.buckets[key_hash]

        key_found = bucket.find(lambda item: item[0] == key)
        if key_found is not None:
            return key_found[1]

        raise KeyError("Key not in hashtable")

    def set(self, key, value):
        """Insert or update the given key with its associated value."""
        # TODO: Insert or update the given key-value entry into a bucket
        key_hash = self._bucket_index(key)
        bucket = self.buckets[key_hash]

        # code from Elmer
        # if self.contains(key):
        #     self.buckets[index] = (key, value)
        # else:
        #     self.buckets[index].append((key, value))
        current = bucket.head
        while (current):
            # update the value with a new tuple if already in bucket
            if current.data[0] == key:
                current.data = (key, value)
                return
            current = current.next
        # otherwise, add the new tuple using the linked list append function
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError."""
        # TODO: Find the given key and delete its entry if found
        key_hash = self._bucket_index(key)
        value_doomed = self.get(key)
        self.buckets[key_hash].delete((key, value_doomed))


def test_hash_table():
    """Tests hashtable."""
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
