# TODO решите задачу
import json


def task(file_input):
    sum_ = 0
    with open("file_input", "r", encoding="utf-8") as file_r:
        data = json.load(file_r)
        for item in data:

            sum_ += item.get("score", 0) * item.get("weight", 0)
        return round(sum_, 3)


print(task(r'input.json'))
