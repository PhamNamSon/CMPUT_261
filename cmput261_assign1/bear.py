"""
Solution stub for the Bear Problem.

Fill in the implementation of the `Bear_problem` class to match the
representation and heuristic that you specified in questions (2a) and (2c).

We will test your solution by calling ``python3 bear.py`` from the shell
prompt.  DO NOT EDIT the main() function.  You may add additional tests to the
`unit_tests` function if you desire.
"""

from heapq import heappop, heappush
from itertools import combinations


class Bear_problem(object):
    def __init__(self):
        self.researchers = {
            "Undergrad": 1.5,
            "Grad Student": 3,
            "Postdoc": 7.5,
            "Professor": 10
        }

        self.start_state = (
            frozenset(["Undergrad", "Grad Student", "Postdoc", "Professor"]),
            frozenset(),
            "Left"
        )

        self.end_state = (
            frozenset(),
            frozenset(["Undergrad", "Grad Student", "Postdoc", "Professor"]), 
            "Right"
        )

    def start_node(self):
        """returns start node"""
        return self.start_state

    def is_goal(self, node):
        """is True if `node` is a goal"""
        return node == self.end_state

    def neighbors(self, node):
        """returns a list of the arcs for the neighbors of `node`"""
        left_side, right_side, light_position = node
        neighbors = []

        if light_position == "Left":
            current_side, other_side, next_light = left_side, right_side, "Right"
        else:
            current_side, other_side, next_light = right_side, left_side, "Left"

        for moving_group in [{r} for r in current_side] + [set(p) for p in combinations(current_side, 2)]:
            new_current = current_side - moving_group
            new_other = other_side | moving_group
            next_state = (frozenset(new_current), frozenset(new_other), next_light)
            neighbors.append((node, next_state))

        return neighbors

    def arc_cost(self, arc):
        """Returns the cost of `arc`"""
        current_state, next_state = arc
        if current_state is None:
            return 0

        left_X, right_X, light_X = current_state
        left_Y, right_Y, light_Y = next_state

        if light_X == "Left" and light_Y == "Right":
            moved_researchers = right_Y - right_X
        elif light_X == "Right" and light_Y == "Left":
            moved_researchers = left_Y - left_X
        else:
            return 0

        return max(self.researchers[person] for person in moved_researchers) if moved_researchers else 0

    def cost(self, path):
        """Returns the cost of `path`"""
        return sum(self.arc_cost(arc) for arc in path)

    def heuristic(self, node):
        """Returns the heuristic value of `node`"""
        left_side, right_side, light = node
    
        if not left_side:
            return 0

        if len(left_side) == 1:
            return self.researchers[next(iter(left_side))]

        costs = sorted([self.researchers[person] for person in left_side], reverse=True)

        return sum(costs[:2]) if len(costs) > 1 else costs[0]

    def search(self):
        """Return a solution path"""
        frontier = Frontier()
        start_node = self.start_node()
        frontier.add([(None, start_node)], 0)  
        explored = set()

        while not frontier.is_empty():
            path = frontier.remove()
            _, current_node = path[-1]  

            if self.is_goal(current_node):
                return path[1:]

            if current_node in explored:
                continue

            explored.add(current_node)

            for arc in self.neighbors(current_node):
                new_path = path + [arc]
                total_cost = self.cost(new_path) + self.heuristic(arc[1])
                frontier.add(new_path, total_cost)

        return None


class Frontier(object):
    """
    Convenience wrapper for a priority queue usable as a frontier
    implementation.
    """

    def __init__(self):
        self.heap = []

    def add(self, path, priority):
        """Add `path` to the frontier with `priority`"""
        # Push a ``(priority, item)`` tuple onto the heap so that `heappush`
        # and `heappop` will order them properly
        heappush(self.heap, (priority, path))

    def remove(self):
        """Remove and return the smallest-priority path from the frontier"""
        priority, path = heappop(self.heap)
        return path

    def is_empty(self):
        return len(self.heap) == 0


def unit_tests():
    """
    Some trivial tests to check that the implementation even runs.
    Feel free to add additional tests.
    """
    print("testing...")
    p = Bear_problem()
    assert p.start_node() is not None
    assert not p.is_goal(p.start_node())
    assert p.heuristic(p.start_node()) >= 0

    ns = p.neighbors(p.start_node())
    assert len(ns) > 0

    soln = p.search()
    assert p.cost(soln) > 0
    print("tests ok")


def main():
    unit_tests()
    p = Bear_problem()
    soln = p.search()
    if soln:
        print("Solution found (cost=%s)\n%s" % (p.cost(soln), soln))
    else:
        raise RuntimeError("Empty solution")


if __name__ == "__main__":
    main()
