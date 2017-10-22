from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets: # Linear time
            for key, value in bucket.items(): # Linear time
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        all_values = []

        # Collect all values in each of the bucket
        for bucket in self.buckets: # Linear time
            for key, value in bucket.items(): # Linear time
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        all_items = []

        # Collect all pairs of key-value entries in each of the buckets
        for bucket in self.buckets: # Linear time
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        length = 0

        # Count number of key-value entries in each of the buckets(linked lists)
        for bucket in self.buckets: # Linear time
            length += bucket.length()
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        hash_index = self._bucket_index(key)
        bucket = self.buckets[hash_index]

        # Check if the given key exists in a bucket
        key_found = bucket.find(lambda item: item[0] == key)
            
        if key_found:
            return True
        return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        hash_index = self._bucket_index(key)
        bucket = self.buckets[hash_index]

        # Check if the given key exists and return its associated value
        key_found = bucket.find(lambda item: item[0] == key)

        if key_found is not None: 
            return key_found[1]

        raise KeyError("Key[{}] not in hashtable".format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        hash_index = self._bucket_index(key)
        bucket = self.buckets[hash_index]

        # Delete given key-value entry if present in linked list
        if self.contains(key):
            self.delete(key)

        # Used 'prepend' to keep most updated 'key-value' pairs close to 'head' of linked list.
        bucket.prepend((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        hash_index = self._bucket_index(key)
        bucket = self.buckets[hash_index]

        key_found = bucket.find(lambda item: item[0] == key)

        if key_found is not None:
            bucket.delete(key_found)
        else:
            raise KeyError("Key[{}] not in hashtable".format(key))


def test_hash_table():
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