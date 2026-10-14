# Case Study 5: Dictionary using hash table and separate chaining

class HashDictionary:
    def __init__(self, size=7):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, word):
        return sum(ord(char.lower()) for char in word) % self.size

    def add(self, word, meaning):
        index = self._hash(word)
        for entry in self.buckets[index]:
            if entry[0].lower() == word.lower():
                entry[1] = meaning
                print(f"Updated '{word}' at bucket {index}.")
                return
        self.buckets[index].append([word, meaning])
        print(f"Added '{word}' at bucket {index}.")

    def search(self, word):
        for stored_word, meaning in self.buckets[self._hash(word)]:
            if stored_word.lower() == word.lower():
                return meaning
        return None

    def delete(self, word):
        bucket = self.buckets[self._hash(word)]
        for i, entry in enumerate(bucket):
            if entry[0].lower() == word.lower():
                del bucket[i]
                return True
        return False

    def display(self):
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket if bucket else '[]'}")


if __name__ == "__main__":
    dictionary = HashDictionary()
    dictionary.add("algorithm", "A step-by-step procedure to solve a problem.")
    dictionary.add("binary", "A number system using 0 and 1.")
    dictionary.add("graph", "A structure made of vertices and edges.")
    dictionary.add("heap", "A tree-based structure for priority operations.")
    dictionary.add("queue", "A FIFO data structure.")
    dictionary.add("stack", "A LIFO data structure.")

    print("\nSearch 'graph':", dictionary.search("graph"))
    print("Search 'tree':", dictionary.search("tree") or "Word not found")
    print("\nHash table buckets (collisions share a bucket):")
    dictionary.display()
    print("\nDelete 'binary':", dictionary.delete("binary"))
    print("Search 'binary' after deletion:", dictionary.search("binary") or "Word not found")
