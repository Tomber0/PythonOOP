import random
class Messeger(object):
    def HelloWorld(self):
        print('Добро пожаловать в месседжер v.012-01')

    def ShowMenu(self):
        print('Меню:\n1-Добавить контакт\n2-Покупки\n3-онлайн-банкинг\n4-настройки\n5-записная книжка\n0-Выход')
    def Setgs(self,Me):
        print('Меню настроек:\n1-изменить аккаунт\n2-Информация об аккаунте\n0-Выход')
        SetCh = int(input('Ваш выбор:'))
        if SetCh == 1:
            Me.Contreset()
        elif SetCh == 2:
            Me.ShowContact()

    def ShowUpdates(self):
        print('ground control to major tom')

class Contact(object):
    def __init__(self,name,number, email, type, balance):
        self.name = name
        self.number = number
        self.email = email
        self.type = type # 0 - сам        1 - контакт        2 - магазин        3        банк
        if self.type == 0:
            self.balance = 50
        else:
            self.balance = 5000

    def Contreset(self):
        self.name = input('Введите новое имя')
        self.number = input('Введите новый номер')
        self.email = input('Введите новый email')

    def ShowContact(self):
        print('Имя - ' + self.name)
        print('Номер - ' + self.number)
        print('Почта - ' + self.email)
        print('Баланс - ' + str(self.balance))


    def ChangeType(self):
        self.type = input('Новый тип - ')

    def Regist(self):
        self.name = input('Введите имя')
        self.number = input('Введите номер')
        self.email = input('Введите email')
        self.type = 0

    def NewContact(self):
        self.name = input('Введите имя')
        self.number = input('Введите номер')
        self.email = input('Введите email')
        self.type = 1

    def ShowAllContacts(self,PhoneBook):
        for items in PhoneBook:
            print('Имя-' + items.name)
            print('\nпочта' + items.email)
            print('\nтелефон' + items.number)
            print('\nТип:\n')
            if items.type == 1 :
                print('обычный\n')

            elif items.type == 2 :
                print('Магазин\n')
            elif items.type == 3:
                print('Банк\n')
            else  :
                print('ошибка\n')

class product(object):
    def __init__(self,name, price):
        self.name = name
        self.price = price
    def ShowProduct(self):
        print('Имя - '+str(self.name))
        print('Цена - '+str(self.price))

class StoreClass(object):
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.inv = []
        self.balance = 50

    def CheckStore(self):
        name = input('Ваш выбор:')
        count = 0

        for item in self.inv:
            if item.name == name:
                count +=1
            if count == 0:
                print('товар не найден в каталоге!\nПроверьте в другой раз')


            else:
                print('товар найден в каталоге!')

    def ShowAll(self):

        for i in range(0,15):
            print(str(self.inv[i].name) + '\n')

    def AddBunchOfItems(self,n):
        namesforprods = ['Рыба', 'Кружки', 'Телефон', 'Лампы']
        for i in range (0,n):
            item = product(namesforprods[random.randint(0,3)],random.randint(10,100))
            self.inv.append(item)

    def Buy(self,Me):
        SInd = -1
        index=-1
        name = input('Ваш выбор:')
        for item in self.inv:
            index+=1
            if (item.name == name):
                    print('товар найден в каталоге!')
                    SInd = index

        if (SInd == -1):
            print('товар не найден в каталоге!\nПроверьте в другой раз')
            return
        print('Стоимость товара ' + str(self.inv[SInd].price) + ' у вас только' + str(Me.balance))
        if (self.inv[SInd].price >= Me.balance):
            print('Недостаточно средств!')
        else:
            Me.balance -= self.inv[SInd].price
            print('Покупка совершена успешно!')

    def ShopMenu(self,Me):
        print('Меню:\n1-Показать товары\n2-Найти товар\n3-Купить\n0-Выход')
        SetCh = int(input('Ваш выбор:'))
        if SetCh == 1:
            self.ShowAll()
        if SetCh ==  2:
            self.CheckStore()
        if SetCh ==  3:
            self.Buy(Me)
class BankClass(object):
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.balance = 50000
    def SetUpGibs(self,Me,PhoneBook):
        inx=0
        inx2=0
        NameOfTaker = input('Введите имя получателя')
        for items in PhoneBook:

            if (items.name == NameOfTaker):
                print('Пользователь с таким именем найден!')
                inx = inx2
            inx2 += 1
        self.Gibs(Me, PhoneBook[inx])
    def 	Gibs(self,FromWho, ToWho):
        tokens = int(input('Введите количество денег для: '+ToWho.name))
        if (tokens<=0):
            print('Недопустимое значение!')

        else :
            FromWho.balance -= tokens
            ToWho.balance += tokens

def main():
    MesMain =  Messeger()
    MesMain.HelloWorld()
    print('Пожалуйста, зарегестрируйте аккаунт')
    Me =  Contact('', '', '', 0, 500)
    Me.Regist()
    contacts = []
    choise = 0
    running = True
    Bank =  BankClass('EuroTrust', 'EuroTrust@gmail.com')

    Store =  StoreClass('EuroOpt', 'EuroOpt@gmail.com')
    Store.AddBunchOfItems(15)

    while (running):
        MesMain.ShowMenu()
        choise = int(input('Ваш выбор:'))

        if choise == 1:
            sampleCont =Contact('', '', '', 0, 50)
            sampleCont.NewContact()
            contacts.append(sampleCont)

        if choise == 2:
            Store.ShopMenu(Me)


        if choise == 3:
            Bank.SetUpGibs(Me, contacts)


        if choise == 4:
            MesMain.Setgs(Me)

        if choise == 5:
            Me.ShowAllContacts(contacts)

        if choise == 0:
            print('Выключение...')
            running = False

        else:
            print('проверьте ввод')

if __name__ == '__main__':
    main()