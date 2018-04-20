class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        try:
            self.queue.pop(0)
        except IndexError:
            print("Empty Queue")

    def peek(self):
        return self.queue[0]

    def size(self):
        print(len(self.queue))

    def __str__(self):
        return str(self.queue)

queue = Queue()
print(queue)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print("Queue: ", queue)

print("Peek: ", queue.peek())

queue.dequeue()
print("Queue after dequeue: ", queue)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue() # Empty Queue
