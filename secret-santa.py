import os
import random
import shutil
from copy import deepcopy


class Santa:
    name: str
    partner: str
    assigned: str | None = None

    def __init__(self, name, partner):
        self.name = name
        self.partner = partner


def try_assignment(santas: list[Santa]) -> bool:
    assignments_path = "./assignments/"
    if os.path.exists(assignments_path):
        shutil.rmtree(assignments_path)

    unassigned = deepcopy(santas)

    for santa in santas:
        valid_ua = list(
            filter(
                lambda u: u.name != santa.name and u.name != santa.partner, unassigned
            )
        )
        if len(valid_ua) == 0:
            return False
        santa.assigned = random.choice(valid_ua).name

        filename = f"./assignments/{santa.name}.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode="w", encoding="utf-8") as out_file:
            out_file.write(santa.assigned)
            out_file.close()
        unassigned = list(filter(lambda u: u.name != santa.assigned, unassigned))

    return True


if __name__ == "__main__":
    with open("santas.txt", encoding="utf-8") as in_file:
        santa_lines = in_file.readlines()
        random.shuffle(santa_lines)
        santas = [
            Santa(name=line.split()[0], partner=line.split()[1]) for line in santa_lines
        ]

        while not try_assignment(santas):
            print("Whoops! Trying again!")
        print("Success!")
        in_file.close()
