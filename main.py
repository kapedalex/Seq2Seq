from Resources.Constants import Constants
from Generation import Generator
from Training import Train

train = Train()
generator = Generator()
print(Constants.GREETING)

match input():
    case '1':
        train.train()
    case '2':
        generator.generate()
    case '3':
        train.train_continue()
    case _:
        raise ValueError(Constants.ERROR)
