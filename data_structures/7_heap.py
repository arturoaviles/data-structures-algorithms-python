import heapq

# Create Heap
heap = [27, 1, 45, 78, 3, 5]

heapq.heapify(heap)
print("Heap: ", heap)

heapq.heappop(heap)
print("Pop", heap)

heapq.heappush(heap, 100)
print("Push 100: ", heap)

heapq.heapreplace(heap, 8)
print("Replace: ", heap)

heapq.heappushpop(heap, 90)
print("Push, Pop: ", heap)