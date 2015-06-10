python3 -m cProfile main.py

So it looks like if we want to make it faster, we need to improve `laplacian.py:get_row_indices`.
Would be interesting to see how much faster numpy could handle this.
We should check it out in a branch.
