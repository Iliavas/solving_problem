from typing import Callable, List
import tkinter as tk
import tkinter.scrolledtext as s

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
        self.create_button = tk.Button(text='generate', width=20, command=self.get_solving)
        self.input_start = tk.Label(text='введи начальное число')
        self.input_start_input = tk.Entry()
        self.command_count = tk.Label(text='сколько команд')
        self.command_count_input = tk.Entry()
        self.target = tk.Label(text='Какое число получить')
        self.target_input = tk.Entry()
        self.get_comm = tk.Label(text='введи команды каждую на своей строке вида x + 1 или x ** 2')
        self.get_comm_input = s.ScrolledText(height=5)
        self.result = tk.Label(text='результат (заполнять не нужно) программа сюда вставит последовательность номеров '
                                    'команд')
        self.result_inp = tk.Entry()


        self.input_start.pack()
        self.input_start_input.pack()
        self.command_count.pack()
        self.command_count_input.pack()
        self.target.pack()
        self.target_input.pack()
        self.get_comm.pack()
        self.get_comm_input.pack()

        self.result.pack()
        self.result_inp.pack()

        self.create_button.pack()

    def get_solving(self):
        first_n = int(self.input_start_input.get())
        c_comm = int(self.command_count_input.get())
        target_v = int(self.target_input.get())
        commands = self.parsing(self.get_comm_input.get('1.0', tk.END).split('\n'))
        gen = Generator(commands, first_n)
        self.printing(gen(c_comm, target_v))

    def parsing(self, l: List[str]) -> List[Callable]:
        return [eval('lambda x: {}'.format(i)) for i in l if i != '']
    def printing(self, string):
        self.result_inp.delete(0, tk.END)
        self.result_inp.insert(0, string)



# HOWTO USE


gen = Generator([lambda x: x + 1, lambda x: x * 2], 6)

print(gen(4, 29))
r = tk.Tk()
root = R(r)
r.mainloop()