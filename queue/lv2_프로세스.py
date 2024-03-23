from collections import deque


def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        # 현재 문서의 인덱스와 중요도
        current = queue.popleft()
        # 나머지 문서 중에 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
        if any(current[1] < other[1] for other in queue):
            queue.append(current)  # 현재 문서를 맨 뒤로 보낸다
        else:
            count += 1  # 인쇄한다
            if current[0] == location:  # 요청한 문서라면 함수 종료
                return count
