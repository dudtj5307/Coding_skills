def solution(todo_list, finished):
    answer = []
    for todo, f in zip(todo_list, finished):
        if not f: answer.append(todo)
    return answer