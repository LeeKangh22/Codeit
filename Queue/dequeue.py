from collections import deque

queue = deque()

#큐의 맨 끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

print(queue)

print(queue[0])

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)