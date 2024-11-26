# TODO импортировать необходимые молули

import json
import csv
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r", encoding="utf-8") as q:
        reader = csv.DictReader(q)
        c = [row for row in reader]
    # TODO Сериализация в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as u:
        json.dump(c, u, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, "r", encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
