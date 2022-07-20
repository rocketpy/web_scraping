import time
import requests
from tqdm import tqdm


URL = 'https://'  # API url

class Api:
    def __init__(self, url: str):
        self.url = url

    def http_get(self, path: str, times: int):
        content = []
        for _ in tqdm(range(times), desc='Fetching data...', colour='GREEN'):
            response = requests.get(self.url + path)
            content.append(response.json())
        return content


if __name__ == '__main__':
    req_times = 10
    api = Api(URL)
    start_timestamp = time.time()
    print(api.http_get(path='fact/', times=req_times))
    task_time = round(time.time() - start_timestamp, 2)
    rps = round(req_times / task_time, 1)
    print(f"| Requests: {req_times}; Total time: {task_time} s; RPS: {rps}. |\n")

