total = 0
total_list = []

for _ in range(4):
    get_out, get_in = map(int, input().split())

    total += get_in - get_out
    total_list.append(total)

print(max(total_list))