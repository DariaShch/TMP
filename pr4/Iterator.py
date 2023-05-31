from collections.abc import Iterator, Iterable


class IteratorTry(Iterator):
   _position: int = None
   _reverse: bool = False

   def __init__(self, collection, reverse=False):
       self._collection = sorted(collection)
       self._reverse = reverse
       self._position = -1 if reverse else 0

   def __next__(self):
       try:
           value = self._collection[self._position]
           self._position += -1 if self._reverse else 1
       except IndexError:
           raise StopIteration()
       return value


class Collection(Iterable):
   def __init__(self, collection):
       self._collection = collection

   def __iter__(self):
       return IteratorTry(self._collection)

   def reverse_it(self):
       return IteratorTry(self._collection, True)


if __name__ == "__main__":
   col = Collection(["Is", "anyone", "here", "?"])
   print(list(col))
   print(list(col.reverse_it()))
