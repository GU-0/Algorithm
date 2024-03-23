from collections import deque


def solution(priorities, location):
    queue = deque([(i, j) for i, j in enumerate(priorities)])  # [index, priority]

    cnt = 0
    while queue:
        a, b = queue.popleft()
        if any(b < item[1] for item in queue):
            queue.append((a, b))
        else:
            cnt += 1
            if a == location:
                return cnt

    return cnt
