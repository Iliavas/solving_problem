from typing import Callable, List
import tkinter as tk

class Generator:
    def __init__(self, commands: List[Callable], start: int):
        self.commands = commands
        self.start = start

    def __call__(self, deph, target):
        res = [[i(self.start) for i in self.commands]]
        res_pos = [[i + 1 for i in range(len(self.commands))]]
        while deph - 1:
            deph -= 1
            local_res = []
            local_res_pos = []
            for j in res[-1]:
                for pos, elem in enumerate(self.commands):
                    local_res.append(elem(j))
                    local_res_pos.append(pos + 1)
            res.append(local_res)
            res_pos.append(local_res_pos)
        first_pos = -1
        print(res)
        for pos, elem in enumerate(res[-1]):
            if elem == target: first_pos = pos
        if first_pos == -1: return None
        counter = 2
        tgs = [first_pos]
        for i in list(reversed(list(map(lambda x: len(x), res))))[1:]:
            first_pos //= len(self.commands)
            counter += 1
            tgs.append(first_pos)
        res = []
        for pos, elem in enumerate(list(reversed(tgs))):
            res.append(res_pos[pos][elem])

        return ''.join(map(str, res))

class R:
    def __init__(self, master):
        self.master = master
        super().__init__()


# HOWTO USE


gen = Generator([lambda x: x + 1, lambda x: x * 2], 6)

print(gen(4, 29))
r = tk.Tk()
root = R(r)
r.mainloop()