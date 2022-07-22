T = int(input())
room_list = []
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = 0
    room = 1
    count = 0
    
    for _ in range(N):
        floor += 1
        count += 1
        if count == N:
            floor = str(floor)
            if room < 10:
                room = str(room)
                room = '0' + room
                room_list.append(floor+room)
                room = int(room)
            else:
                room = str(room)
                room_list.append(floor+room)
                room = int(room)
        if int(floor) >= H:
          floor = 0
          room += 1

for x in room_list:
  print(x)