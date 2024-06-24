from datetime import datetime

# 입력 받기
n = int(input())

weather_data = []

for _ in range(n):
    data = input().split()
    date_str = data[0]
    day = data[1]
    weather = data[2]
    weather_data.append((date_str, day, weather))

# 초기화
earliest_rain_date = None
earliest_rain_info = None

# 날짜 비교
for date_str, day, weather in weather_data:
    if weather == "Rain":
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if earliest_rain_date is None or date < earliest_rain_date:
            earliest_rain_date = date
            earliest_rain_info = (date_str, day, weather)

# 결과 출력
if earliest_rain_info:
    print(" ".join(earliest_rain_info))