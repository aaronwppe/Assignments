class Switch:
    def __init__(self, default_string="Invalid Input!", break_line=("=" * 20)):
        self.count = 0
        self.options_list = list()
        self.switch_dict = dict()
        self.default_string = default_string
        self.break_line = break_line

    def add_case(self, string: str, func):
        if not callable(func):
            return

        self.count += 1
        self.options_list.append(f"{self.count}. {string}")
        self.switch_dict[self.count] = func

    def exit_program(self):
        print('Bye!')
        print(self.break_line)
        exit()

    def run(self):
        self.add_case("Exit", lambda: self.exit_program())

        print("Options:")
        for i in self.options_list:
            print(i)

        while 1:
            option = input("Perform: ")
            if option.isnumeric():
                option = int(option)
            else:
                # invalid option
                option = 0
            func = self.switch_dict.get(option, lambda: print(self.default_string))
            func()
            print(self.break_line)


# Reference code:
# switch = switch.Switch2()
# switch.add_exit_case()
#
# print("Options:")
# print(switch.options)
#
# while not switch.exit_is_selected:
#     option = input("Perform: ")
#     print(switch.run(option))
class Switch2:
    def __init__(self, default_string="Invalid Input!", break_line=("=" * 20)):
        self.count = 0
        self.options_list = list()
        self.switch_dict = dict()
        self.default_string = default_string
        self.break_line = break_line
        self.exit_is_selected = False

    def add_case(self, string: str, func):
        if not callable(func):
            return

        self.count += 1
        self.options_list.append(f"{self.count}. {string}")
        self.switch_dict[self.count] = func

    @property
    def options(self):
        ret = str()
        for i in self.options_list:
            ret += str(i)

        return ret

    def on_exit(self):
        self.exit_is_selected = True
        return 'Bye!\n' + self.break_line

    def add_exit_case(self):
        self.add_case('Exit', lambda: self.on_exit())

    def run(self, option):
        if not option.isnumeric():
            return self.default_string

        func = self.switch_dict.get(int(option), lambda: self.default_string)

        return func()
