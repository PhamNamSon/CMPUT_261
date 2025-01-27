"""
Solution stub for the Bear Problem.

Fill in the implementation of the `Bear_problem` class to match the
representation and heuristic that you specified in questions (2a) and (2c).

We will test your solution by calling ``python3 bear.py`` from the shell
prompt.  DO NOT EDIT the main() function.  You may add additional tests to the
`unit_tests` function if you desire.
"""

from heapq import heappop, heappush


class Bear_problem(object):
    def __init__(self):
        pass

    def start_node(self):
        """returns start node"""
        # TODO
        return (None,)

    def is_goal(self, node):
        """is True if `node` is a goal"""
        # TODO
        return False

    def neighbors(self, node):
        """returns a list of the arcs for the neighbors of `node`"""
        # TODO
        return []

    def arc_cost(self, arc):
        """Returns the cost of `arc`"""
        # TODO
        return 0

    def cost(self, path):
        """Returns the cost of `path`"""
        return sum(self.arc_cost(arc) for arc in path)

    def heuristic(self, node):
        """Returns the heuristic value of `node`"""
        # TODO
        return 0

    def search():
        """Return a solution path"""
        # TODO
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
