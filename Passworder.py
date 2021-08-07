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
            minusculas = ['a', 'b', 'c', 'e', 'd', 'f', 'i', 'k', 'j', 'm', 'n', 'l', "ñ", 'o', 'p', 'q', 'r', 's', 't',
                          'u', 'v', 'w', 'y', 'z']
            self.Selector.append(minusculas)
            return True
        else:
            return False
    def setMayusculas(self, optionMayus = True):
        if optionMayus:
            minusculas = ['a', 'b', 'c', 'e', 'd', 'f', 'i', 'k', 'j', 'm', 'n', 'l', "ñ", 'o', 'p', 'q', 'r', 's', 't',
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

    def setEspeciales(self,optionEspeciales = True):
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
        return self.PSW

    def Username(self):
        case = randint(0,1)
        self.username = self.nombreBot.replace(' ', '')
        if case == 0:
            self.username = self.username + str(randint(0, 1000))
        else:
            l = randint(8, 20)
            self.username = self.Password(l)


    # def send_to_csv(self,data):
    #     DF = DataFrame(data)
    #     DF.to_csv('BotList.csv', mode='a')

def FakeUser(numofbots):
    for _ in range(0, numofbots):
        _ = Bot()
        _.Nombres()
        _.Password()
        _.Username()
        data = [_.nombreBot, _.apellidoBot, _.PSW, _.username]
        DF = DataFrame(data).T
        DF.to_csv('BotList.csv', mode='a', header=False,index=False)