def solution(new_id):
    new_id = list(new_id)
    ok = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']

    i = 0
    while i < len(new_id):
        asc = ord(new_id[i])
        if 65 <= asc <= 90:     # 대문자
            new_id[i] = new_id[i].lower()

        elif new_id[i] not in ok:
            if asc < 97 or asc > 122:
                new_id.pop(i)
                continue

        elif new_id[i] == '.' and new_id[i-1] == '.':
                new_id.pop(i)
                continue

        i += 1

    if len(new_id) > 0 and new_id[0] == '.':
        new_id.pop(0)

    if len(new_id) > 0 and new_id[-1] == '.':
        new_id.pop()

    if not new_id:
        return 'aaa'

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id.pop()

    if len(new_id) <= 2:
        last = new_id[-1]
        while len(new_id) != 3:
            new_id.append(last)

    return ''.join(map(str, new_id))
