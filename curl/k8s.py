import base64
import random
import time
from concurrent.futures import ThreadPoolExecutor

import cv2
import requests

SERIAL = True
RANDOM = False

URL = "http://zerohertz.xyz:80/"

HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
}


def prepare_data(IMAGE_PATH="test.jpg"):
    img = cv2.imread(IMAGE_PATH)
    _, buffer = cv2.imencode(".jpg", img)
    DATA = {
        "img": base64.b64encode(buffer).decode("utf-8"),
    }
    return DATA


def send_request(HEADERS, DATA, RANDOM=False):
    if RANDOM:
        time.sleep(random.randrange(0, 20))
    response = requests.post(URL, headers=HEADERS, json=DATA, verify=False)
    res = response.json()
    print(f"""TOTAL: {res["process_time"]:.2f}""")
    print(res["results"][0])
    return str(res["process_time"]) + "\n"


def main(DATA, SESSION):
    DATA = prepare_data()
    max_workers = 100

    START = time.time()
    if SERIAL:
        FILE_NAME = "SERIAL"
        responses = []
        for _ in range(max_workers):
            responses.append(send_request(HEADERS, DATA))
    else:
        if RANDOM:
            FILE_NAME = "RANDOM"
        else:
            FILE_NAME = "CONCURRENCY"
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            responses = list(
                executor.map(
                    send_request,
                    [HEADERS] * max_workers,
                    [DATA] * max_workers,
                    [RANDOM] * max_workers,
                )
            )
    END = time.time()
    print("=" * 10, END - START, "=" * 10)
    with open(f"{FILE_NAME}_{SESSION}.txt", "w") as f:
        f.writelines(responses)
        f.writelines(str(END - START) + "\n")


if __name__ == "__main__":
    for i in range(10):
        main(i)
        time.sleep(10)
