# TODO решите задачу
import json

def task() -> float:

    sum_ = 0
    with open("input.json", "r", encoding="utf-8") as file_r:
        data = json.load(file_r)

        for item in data:
           number1 = item.get("score", 0)
           number2 = item.get("weight", 0)

           if number1 and number2:
            sum_ += number1 * number2

    return round(sum_, 3)

print(task())
