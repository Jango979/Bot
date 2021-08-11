import Passworder as ps
from pandas import read_csv
from parte1 import parte1


def main(Numero_de_Bots=40):
    ps.FakeUser(Numero_de_Bots)
    DF = read_csv('BotList.csv', header=None)
    parte1(DF)


if __name__ == '__main__':
    main(40)


