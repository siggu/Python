x, y = map(int, input().split())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

today_days = 0

for i in range(x - 1):
    today_days += months[i]
    
today_days = (today_days + y) % 7

print(days[today_days])