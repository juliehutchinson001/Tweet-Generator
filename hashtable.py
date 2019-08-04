from linked_list import Linked_list


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [Linked_list() for _ in range(init_size)]
        # Another way to do append to an array
        # map(lambda _: Linked_list(), init_size)

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, _ in bucket.items():

                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(BL) Why and under what conditions?"""
        all_values = []
        for bucket in self.buckets:
            for _, value in bucket.items():

                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets."""
        # result = 0
        # for bucket in self.buckets:
        #     result += bucket.length()

        return sum([bucket.length() for bucket in self.buckets])

    def contains(self, key):
        """Return True if this hash table contains the given key, or False."""
        bucket_index = self._bucket_index(key)
        # ------example for callback----------
        # def callback(item):
        #     if key == item:
        #         return True
        #     return False

        # found = self.buckets[bucket_index].find(callback)
        # -------------------------------------
        found = self.buckets[bucket_index].find(lambda item: key == item)
        return True if found != None else False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError."""
        # if value != None:
        #     return value[1]
        # else:
        #     raise KeyError('Key not found: {}'.format(key))
        def raise_error():
            raise KeyError('Key not found: {}'.format(key))

        bucket_index = self._bucket_index(key)
        value = self.buckets[bucket_index].find(lambda item: key == item)

        # one liner
        # return value[1] if value != None else 'Key not found'
        return value[1] if value != None else raise_error()

    def set(self, key, value):
        """Insert or update the given key with its associated value."""

        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        found = bucket.find(lambda item: key == item)
        if found != None:
            bucket.delete((found[0], found[1]))
            bucket.append((key, value))
        else:
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError."""

        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        found = bucket.find(lambda item: key == item)
        if found != None:
            bucket.delete((found[0], found[1]))
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    HashTable(object)

    '''
    Visual representation of a hashtable

    [ [], [], [] ] = ht
      |   |   |
      LL  LL  LL

    '''
