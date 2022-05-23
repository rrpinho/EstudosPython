class Deque:
    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False
    
    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.append(e)
        self.len += 1
    
    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.empty():
            self.len -= 1
            self.deque.pop(self.len)

    def front(self):
        if not self.empty():
            return self.deque[0]
    
    def back(self):
        if not self.empty():
            return self.deque[-1]

    def show(self):
        for i in self.deque:
            print(i, end = ' ')
        print()

    def lenght(self):
        return self.len

d = Deque()
print(d.empty())
d.push_front(2)
d.push_front(1)
d.push_back(3)
d.show()
print(d.empty())
print(d.lenght())
print(d.front())
print(d.back())
d.pop_front()
d.pop_back()
d.show()
print(d.front())
print(d.back())
d.pop_back()
print(d.empty())
print(d.lenght())