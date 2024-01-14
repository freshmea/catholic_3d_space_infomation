# author: choi sugil
# date: 2023.10.25 version: 1.0.0 license: MIT brief: keyward
# description: 데이터클래스 와 클래스를 연동하는 프로그램 json 으로 데이터를 읽어옴
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd


@dataclass
class StudentArg:
    """Data class for student."""

    name: str
    korean: int = 0
    math: int = 0
    english: int = 0
    science: int = 0
    score_set: list = field(default_factory=list)

    def __post_init__(self):
        """_summary_."""
        self.score_set = [self.korean, self.math, self.english, self.science]


class Student:
    def __init__(self, arg: StudentArg):
        """student class
        Args:
            args (StudentArg): Student dataclass

        Attributes:
            name: str
            korean: int
            math: int
            english: int
            science: int
            score_set: list
        """
        self.name = arg.name
        self.korean = arg.korean
        self.math = arg.math
        self.english = arg.english
        self.science = arg.science
        self.score_set = arg.score_set

    def get_sum(self):
        return sum(self.score_set)

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average():.2f}"


def main():
    param_dir = r"C:\chungnam_chatbot\python"
    students = []
    params = pd.read_csv(Path(param_dir) / "params.csv")
    print(params.info())

    for i in range(len(params)):
        param = dict(params.iloc[i, :])
        arg = StudentArg(**param)  # type: ignore
        students.append(Student(arg))
        print(f"{students[-1].name} : {students[-1].score_set}")

    print("이름\t총점\t평균")
    for student in students:
        print(student)


if __name__ == "__main__":
    main()