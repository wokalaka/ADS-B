import requests  
import json  
  
# 定义经纬度范围  
lon_min, lat_min = -180.00, -90.00  
lon_max, lat_max = 180.00, 90.00  
  
user_name = 'wukalaka'  
password = '20040917LiuZheng@'  
  
url_base = 'https://opensky-network.org/api/states/all?'  
params = {  
    'lamin': str(lat_min),  
    'lomin': str(lon_min),  
    'lamax': str(lat_max),  
    'lomax': str(lon_max)  
}  
  
def list_to_dict(data_list, keys):  
    data_dict = {}  
    for key, value in zip(keys, data_list):  
        if value == 'false':  
            value = False  
        elif value == 'null':  
            value = None  
        data_dict[key] = value  
    return data_dict  
  
# 假设的键名列表  
keys = [  
    "icao24", "callsign", "origin_country", "time_position", "last_contact", "lat",  
    "lon", "baro_altitude", "on_ground", "velocity",  
    "true_track", "mach", "vertical_rate", "sensors",  
    "geo_altitude", "squawk", "spi", "position_source"  
]  
  
# 发送请求  
try:  
    response = requests.get(url_base, params=params, auth=(user_name, password))  
    response.raise_for_status()  # 如果请求不成功，将抛出HTTPError异常  
    flight_data = response.json()['states']  
  
    dicts = []  
    for data_list in flight_data:  
        dicts.append(list_to_dict(data_list, keys))  
  
    output_filename = 'flight_data.json'  
  
    # 将字典列表转换为JSON数组，并写入到文件中  
    with open(output_filename, 'w') as outfile:  
        json.dump(dicts, outfile, ensure_ascii=False, indent=4)  # 使用json.dump()并设置缩进以便于阅读  
  
    print(f'Data saved to {output_filename} as a valid JSON array.')  
except requests.RequestException as e:  
    print(f'Error occurred: {e}')  
except json.JSONDecodeError:  
    print('Failed to decode JSON response.')  
except Exception as e:  
    print(f'An unexpected error occurred: {e}')
