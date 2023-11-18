from geopy.distance import geodesic
import math

def generate_coordinates(center_lat, center_lon, radius_meters, num_points):
    # 將經緯度轉換為弧度
    center_lat_rad = math.radians(center_lat)
    center_lon_rad = math.radians(center_lon)

    coordinates = []

    for i in range(num_points):
        # 計算每個點的角度
        angle = 2 * math.pi * i / num_points

        # 計算新點的經緯度
        new_lat_rad = center_lat_rad + (radius_meters / 6371000) * math.sin(angle)
        new_lon_rad = center_lon_rad + (radius_meters / 6371000) * math.cos(angle) / math.cos(center_lat_rad)

        # 將新經緯度轉換為度數
        new_lat = math.degrees(new_lat_rad)
        new_lon = math.degrees(new_lon_rad)

        coordinates.append((new_lat, new_lon))

    return coordinates

# 輸入經緯度以及其他參數
center_latitude = float(input("請輸入中心緯度："))
center_longitude = float(input("請輸入中心經度："))
radius_meters = 50
num_points = 16

# 生成座標
result_coordinates = generate_coordinates(center_latitude, center_longitude, radius_meters, num_points)

# 顯示結果
print("生成的座標點：")
for coordinate in result_coordinates:
    print(coordinate)
print(result_coordinates[0])

