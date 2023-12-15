def solution(new_id):
    answer = ""
    for s in new_id:
        if s.isalpha():
            if ord(s) <= ord('Z'):
                s = chr(ord(s) + ord('a') - ord('A'))
            answer += s
        elif s.isnumeric() or s in ['-','_','.']:
            answer += s
    while '..' in answer:
        answer = answer.replace('..','.')
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.': 
        answer = answer[:-1]
    if answer == "": answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    while len(answer) < 3:
        answer += answer[-1]
    return answer