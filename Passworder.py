#listas
from random import choice,randint
from iteration_utilities import deepflatten
from pandas import DataFrame

class Bot():
    def __init__(self):
        self.Selector = []
        self.setMinusculas()
        self.setMayusculas()
        self.setNumeros()
        self.Selector = list(deepflatten(self.Selector, depth=1))

    def setMinusculas(self,optionMin = True):
        if optionMin:
            minusculas = ['a', 'b', 'c', 'e', 'd', 'f', 'i', 'k', 'j', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'y', 'z']
            self.Selector.append(minusculas)
            return True
        else:
            return False
    def setMayusculas(self, optionMayus = True):
        if optionMayus:
            minusculas = ['a', 'b', 'c', 'e', 'd', 'f', 'i', 'k', 'j', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'y', 'z']

            self.Selector.append([i.upper() for i in minusculas])
            return True
        else:
            return False

    def setNumeros(self,optionNum = True):
        if optionNum:
            self.Selector.append([i for i in range(0, 10)])
            return True
        else:
            return False

    def setEspeciales(self,optionEspeciales = False):
        if optionEspeciales:
            self.Selector.append([' ', '!', "#", '$', "%", "&", "(", ")", "?", "¡","¿", "*", "[", "]", "{", "}", "_", "-", ":", ".", ";"])
            return True
        else:
            return False
    def Nombres(self):
        nombres=['ANTONIO','MANUEL', 'FRANCISCO','JOSE', 'DAVID', 'JUAN', 'JAVIER', 'JOSE', 'ANTONIO', 'DANIEL', 'JOSE','LUIS','FRANCISCO','JAVIER','CARLOS','JESUS','ALEJANDRO',
             'MIGUEL','JOSE','MANUEL','RAFAEL','MIGUEL','ANGEL','PABLO','PEDRO','ANGEL','SERGIO','JOSE','MARIA','FERNANDO','JORGE','LUIS','ALBERTO','ALVARO','JUAN','CARLOS',
             'ADRIAN','DIEGO','JUAN','JOSE','RAUL','IVAN','JUAN','ANTONIO','RUBEN','ENRIQUE','OSCAR','RAMON','ANDRES','VICENTE','JUAN','MANUEL','SANTIAGO','JOAQUIN','VICTOR',
             'MARIO','EDUARDO','ROBERTO','JAIME','FRANCISCO','JOSE','MARCOS','IGNACIO','HUGO','ALFONSO','JORDI','RICARDO','SALVADOR','GUILLERMO','GABRIEL',
             'MARC','EMILIO','MOHAMED','GONZALO','JULIO','JULIAN','MARTIN','JOSE','MIGUEL','TOMAS','AGUSTIN','NICOLAS','JOSE','RAMON','SAMUEL','ISMAEL','JOAN',
             'CRISTIAN','FELIX','LUCAS','AITOR','HECTOR','JUAN','FRANCISCO','IKER','ALEX','JOSE','CARLOS','JOSEP','SEBASTIAN','MARIANO','CESAR','ALFREDO','DOMINGO','JOSE',
             'ANGEL','FELIPE','VICTOR','MANUEL','RODRIGO','JOSE','IGNACIO','MATEO','LUIS','MIGUEL','JOSE','FRANCISCO','JUAN','LUIS','XAVIER','ALBERT']
        apellidos = ['HERNANDEZ','GARCIA','MARTINEZ','LOPEZ','GONZALEZ','RODRIGUEZ','PEREZ','SANCHEZ','RAMIREZ','FLORES','CRUZ','GOMEZ','MORALES','VAZQUEZ','JIMENEZ',
                 'REYES','DIAZ','TORRES','GUTIERREZ','RUIZ','AGUILAR','MENDOZA','CASTILLO','ORTIZ','MORENO','RIVERA','RAMOS','ROMERO','JUAREZ','ALVAREZ','MENDEZ','CHAVEZ','HERRERA',
                 'MEDINA','DOMINGUEZ','CASTRO','GUZMAN','VARGAS','VELAZQUEZ','SALAZAR','ROJAS','ORTEGA','CORTES','SANTIAGO','GUERRERO','CONTRERAS','BAUTISTA','ESTRADA','LUNA','JUNCAL',
                 'JUSTINIANO','JUVENAL','KANAGUSICO','KELLER','KRAUSS','LACARRA','LACARRIERE','LACES']
        if randint(1,2) == 2:
            self.nombreBot = choice(nombres) +' '+choice(nombres)
        else:
            self.nombreBot = choice(nombres)
        if randint(1,2) == 2:
            self.apellidoBot = choice(apellidos) +' '+choice(apellidos)
        else:
            self.apellidoBot = choice(apellidos)


    def Password(self, length=13):
        self.PSW = []
        for i in range(0,length):
            self.PSW.append(choice(self.Selector))
        self.PSW = ''.join(map(str,self.PSW))
        self.PSW = self.PSW + str(randint(10,100000))
        return self.PSW

    def Username(self):
        case = randint(0,1)
        self.username = self.nombreBot.replace(' ', '')
        if case == 0:
            self.username = ''.join(map(str,self.username)) + str(randint(1000000, 10000000000))
            print(self.username)
        else:
            self.username = self.username.replace(' ','') + self.apellidoBot.replace(' ','') + str(randint(100000, 1000000000))
            print(self.username)

    def Country(self):
        Paises = ['DE','AD','AG','AR','BZ','BO','SV','ES','US','GT','IS','MX','ME',
                  'BR','CA','CL','CO','CU','DK','DM','EC','PA','PY','PE','NI','CH','SE',
                  'UZ','VE','UY','VN']
        self.C= choice(Paises)

    # def send_to_csv(self,data):
    #     DF = DataFrame(data)
    #     DF.to_csv('BotList.csv', mode='a')
    def BirthdayDay(self):
        self.bd = str(randint(1,31))
    def BirthdayMonth(self):
        self.bm = str(randint(1,12))
    def BirthdayYear(self):
        self.by = str(randint(1970,2012))

def FakeUser(numofbots):
    for _ in range(0, numofbots):
        _ = Bot()
        _.Nombres()
        _.Password()
        _.Username()
        _.Country()
        _.BirthdayDay()
        _.BirthdayMonth()
        _.BirthdayYear()
        data = [_.nombreBot, _.apellidoBot, _.PSW, _.username, _.C, _.bd, _.bm, _.by]
        DF = DataFrame(data).T
        DF.to_csv('BotList.csv', mode='a', header=False,index=False)