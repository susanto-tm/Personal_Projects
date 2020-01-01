class MinHeap:
    def __init__(self, heap):
        self.heap = heap

    def min_heap(self, arr, i):
        left = 2*i + 1
        right = 2*i + 2
        length = len(arr) - 1
        smallest = i

        if left <= length and arr[i] > arr[left]:
            smallest = left
        if right <= length and arr[i] > arr[right]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.min_heap(arr, smallest)

    def build_min_heap(self):
        for i in reversed(range(len(self.heap)//2)):
            self.min_heap(self.heap, i)

        return self.heap


heap_arr = [1, 9, 8, 2, 3, 10, 14, 7, 16, 4]
min_heap = MinHeap(heap_arr)
print(min_heap.build_min_heap())


