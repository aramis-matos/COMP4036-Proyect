import pandas as pd


class Character:
    def __init__(self, id_num, name):
        self.name = name
        self.id = id_num
        self.moves, self.stats, self.df = Character.get_moves_and_stats(name)

    @staticmethod
    def get_moves_and_stats(name):
        temp_df = pd.read_csv(str(name)+"_fd.csv")
        temp_moves = list(temp_df.columns)
        temp_stats = list(temp_df.index)
        return temp_moves, temp_stats, temp_df

    def print_fd(self):
        for item in range(len(self.moves)):
            print(self.moves[item])
            temp_data = list(self.df[self.moves[item]])
            print("Damage: " + str(temp_data[0]))
            print("Guard: ", end=' ')
            Character.print_block_name(str(temp_data[1]))
            print("Startup: " + str(temp_data[2]))
            print("Active: " + str(temp_data[3]))
            print("Recovery: " + str(temp_data[4]))
            print("On Block: " + str(temp_data[5]))
            print("On Hit: " + str(temp_data[6]))
            print()

    @staticmethod
    def print_block_name(a):
        for k in range(len(a)):
            if a[k] == 'm':
                print("mid", end=' ')
            if a[k] == 'a':
                print("air", end=' ')
            if a[k] == 't':
                print("throw", end=' ')
            if a[k] == 'h':
                print("high", end=' ')
            if a[k] == 'l':
                print("low", end=' ')
            if a[k] == ',':
                print("/", end=' ')
        print()


