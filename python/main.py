from pathlib import Path
from typing import Callable
import day01
import day02

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"

def read_input_file(file_name: str) -> str:
    path = DATA_DIR / (file_name + ".txt")
    return path.read_text(encoding="utf-8")
    
def write_output_file(file_name: str, data: str):
    path = RESULTS_DIR / (file_name + ".txt")
    path.write_text(data, encoding="utf-8")

def solve(file_name: str, run: Callable[[str], str]):
    input = read_input_file(file_name)
    result = run(input)
    write_output_file(file_name, str(result))

Case = tuple[str, Callable[[str], str]]

cases: list[Case] = [
    ("day01-1", day01.run1),
    ("day01-2", day01.run2),
    ("day02-1", day02.run1)
]

for name, run in cases:
    solve(name, run)