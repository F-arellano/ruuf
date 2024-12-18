from greedy import get_greedy_solution
from greedy import get_greedy_solution_triangle

ROOF_SIZE = (7, 10)
PANEL_SIZE = (1, 2)
HEIGHT = 6
BASE = 7
# print("solution: ", get_greedy_solution(ROOF_SIZE, PANEL_SIZE, plot=True))
print("solution: ", get_greedy_solution_triangle(PANEL_SIZE, HEIGHT, BASE, plot=True))
