from collections import deque

kids = deque(["George", "Peter", "Michael", "William", "Thomas"])

print(kids)
kids.rotate(-2)
print(kids)