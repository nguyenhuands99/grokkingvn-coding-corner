'''BusinessTasks (Topcoder):
N tasks are written down in the form of a circular list, so the first task is adjacent to the last one. A number n is also given. Starting with the first task, move clockwise (from element 1 in the list to element 2 in the list and so on), counting from 1 to n. When your count reaches n, remove that task from the list and start counting from the next available task. Repeat this procedure until one task remains. Return it.
'''

def get_final_task(tasks, n):
    pos = 0
    while len(tasks) > 1:
        pos = (pos + (n - 1)) % len(tasks)
        tasks.pop(pos)
        if pos == len(tasks):
            pos = 0
    return tasks[0]

test_case1 = ["a", "b", "c", "d"], 2	 # expect 'a'
test_case2 = 	["alpha", "beta", "gamma", "delta", "epsilon"], 1  # expect 'epsilon'
test_case3 = 	["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], 17  # expect 'n'
test_case4 = 	["zlqamum", "yjsrpybmq", "tjllfea", "fxjqzznvg", "nvhekxr", "am", "skmazcey", "piklp", "olcqvhg", "dnpo", "bhcfc", "y", "h", "fj", "bjeoaxglt", "oafduixsz", "kmtbaxu", "qgcxjbfx", "my", "mlhy", "bt", "bo", "q"], 9000000  # expect 'fxjqzznvg'
print(get_final_task(*test_case4))
