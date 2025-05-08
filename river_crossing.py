from typing import List, Tuple


def solve(N: int, coords: List[Tuple[int, int]]) -> int:
    """
    Given N pairs of start coordinates on the starting bank and finish coordinates
    on the ending bank, returns the maximum number of non crossing-boats, and a list of indices
    representing the set of non-crossing boats that that is as large as possible

    Parameters
    ----------
    N : int
        The number of boats
    coords : List[Tuple[int, int]]
        Pairs of coordinates of form (x, y). x is the possition on the starting bank,
        and y is the position on the ending bank.

    Returns
    -------
    int
        int - Maximum number of non crossing boats.
    """
    assert N == len(coords), f"Expected {N} pairs of coordinates, but found {len(coords)}."
    for i, c in enumerate(coords):
        assert len(c) == 2, f"Every boat should have two coordinates. Instead, boat {i + 1} has {len(c)} elements."

    # TODO: Your code here
    boats = sorted(coords, key=lambda x: (x[0]))
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if boats[i][1] > boats[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    # Return an int (number of boats)
    return max(dp)


def read_input():
    N = int(input())
    coords = [tuple(int(i) for i in input().split()) for _ in range(N)]
    return N, coords


def main():
    N, coords = read_input()
    boats = solve(N, coords)
    print(boats)


if __name__ == '__main__':
    main()
