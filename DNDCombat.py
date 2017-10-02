import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import randint
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret_dnd.json', scope)
client = gspread.authorize(creds)

monstertable = client.open('DnD Combat').sheet1

def new_monster():
    index = monstertable.row_count + 1

    monster = input('Monster Name: ')
    hp = input('Monster Hit Points: ')
    armorclass = input('Armor Class: ')
    stre = input('Strength: ')
    stremod = input('Strength Modifier: ')
    dex = input('Dexterity: ')
    dexmod = input('Dexterity Modifier: ')
    con = input('Constitution: ')
    conmod = input('Constitution Modifier: ')
    inte = input('Intelligence: ')
    intemod = input('Intelligence Modifier: ')
    wis = input('Wisdom: ')
    wismod = input('Wisdom Modifier: ')
    cha = input('Charisma: ')
    chamod = input('Charisma Modifier: ')
    atkname1 = input('First Attack Name: ')
    atkaccu1 = input('First Attack Accuracy: ')
    atkdice1 = input('First Attack Dice: ')
    atkmod1 = input('First Attack Modifier: ')
    atkname2 = input('Second Attack Name("-" for none): ')
    atkaccu2 = input('Second Attack Accuracy("-" for none): ')
    atkdice2 = input('Second Attack Dice("-" for none): ')
    atkmod2 = input('Second Attack Modifier("-" for none): ')
    atkname3 = input('Third Attack Name("-" for none): ')
    atkaccu3 = input('Third Attack Accuracy("-" for none): ')
    atkdice3 = input('Third Attack Dice("-" for none): ')
    atkmod3 = input('Third Attack Modifier("-" for none): ')
    abilities = input('All extra Abilities("-" for none): ')

    infos = [monster, hp, armorclass, stre, stremod, dex, dexmod, con, conmod, inte, intemod, wis, wismod, cha, chamod, atkname1, atkaccu1, atkdice1, atkmod1, atkname2, atkaccu2, atkdice2, atkmod2, atkname3, atkaccu3, atkdice3, atkmod3, abilities]

    monstertable.insert_row(infos, index)

def delete_monster():
    rows = monstertable.row_count
    for i in range(2, rows + 1):
        print(str(i-1) + ')', monstertable.cell(i,1).value)
    dele = int(input('Choose the monster you want to Delete: '))
    if dele > 0 and dele < (rows):
        dmonst = monstertable.cell(dele + 1, 1).value
        deleyn = input('Are you sure you want to delete the monster %s (y/n)?: ' %dmonst)
        if deleyn == 'y':
            monstertable.delete_row(dele + 1)
            print('Monster %s Deleted!' %dmonst)
    else:
        print('There are only %d Monsters in the Data Base!' %(rows-1))

def show_monster_menu():
    rows = monstertable.row_count
    for i in range(2, rows + 1):
        print(str(i-1) + ')', monstertable.cell(i,1).value)
    show = int(input('Choose the monster that you want to see the stats: '))
    show = show + 1
    show_monster(show)

def show_monster(show):
    print()
    print('Monster Name: %s' %(monstertable.cell(show, 1).value))
    print('Hit Points: %s' %(monstertable.cell(show, 2).value))
    print('Armor Class: %s' %(monstertable.cell(show, 3).value))
    print('Strength: %s' %(monstertable.cell(show, 4).value))
    print('Strength Modifier: %s' %(monstertable.cell(show, 5).value))
    print('Dexterity: %s' %(monstertable.cell(show, 6).value))
    print('Dexterity Modifier: %s' %(monstertable.cell(show, 7).value))
    print('Constitution: %s' %(monstertable.cell(show, 8).value))
    print('Constitution Modifier: %s' %(monstertable.cell(show, 9).value))
    print('Intelligence: %s' %(monstertable.cell(show, 10).value))
    print('Intelligence Modifier: %s' %(monstertable.cell(show, 11).value))
    print('Wisdom: %s' %(monstertable.cell(show, 12).value))
    print('Wisdom Modifier: %s' %(monstertable.cell(show, 13).value))
    print('Charisma: %s' %(monstertable.cell(show, 14).value))
    print('Charisma Modifier: %s' %(monstertable.cell(show, 15).value))
    print('First Attack Name: %s' %(monstertable.cell(show, 16).value))
    print('First Attack Accuracy: %s' %(monstertable.cell(show, 17).value))
    print('First Attack Dice: %s' %(monstertable.cell(show, 18).value))
    print('First Attack Modifier: %s' %(monstertable.cell(show, 19).value))
    if ((monstertable.cell(show, 20).value) != '-'):
        print('Second Attack Name: %s' %(monstertable.cell(show, 20).value))
        print('Second Attack Accuracy: %s' %(monstertable.cell(show, 21).value))
        print('Second Attack Dice: %s' %(monstertable.cell(show, 22).value))
        print('Second Attack Modifier: %s' %(monstertable.cell(show, 23).value))
    if ((monstertable.cell(show, 24).value) != '-'):
        print('Third Attack Name: %s' %(monstertable.cell(show, 24).value))
        print('Third Attack Accuracy: %s' %(monstertable.cell(show, 25).value))
        print('Third Attack Dice: %s' %(monstertable.cell(show, 26).value))
        print('Third Attack Modifier: %s' %(monstertable.cell(show, 27).value))
    print('Abilities: %s' %(monstertable.cell(show, 28).value))

def iniciative():
    iniciative_order =[]
    while True:
        rows = monstertable.row_count
        for index in range(2, rows + 1):
            print(str(index-1) + ')', monstertable.cell(index,1).value)
        row_atual = int(input('Choose The Monster: '))
        row_atual = row_atual + 1
        num_monster = int(input('How many %s you want?: ' %(monstertable.cell(row_atual, 1).value)))
        for index in range(1, num_monster + 1):
            numinit = randint(1,20)
            if numinit < 10:
                numinit = '0' + str(numinit)
            else:
                numinit = str(numinit)

            m = numinit + ' ' + monstertable.cell(row_atual, 1).value + ' ' + monstertable.cell(row_atual, 3).value + ' ' + monstertable.cell(row_atual, 2).value
            iniciative_order = iniciative_order + [m]
        choice = input('You want to add another monster (y/n)?: ')
        if choice == 'n' or choice == 'N':
            break
    num_player = int(input('How many players do you want?: '))
    for index in range(1, num_player + 1):
        player_name = input("What is the Player's name?: ")
        player_init = input("What is the Player's initiative?: ")
        if int(player_init) < 10:
            player_init = '0' + player_init
        player_arclass = input("What is the Player's Armor Class?: ")
        player_data = player_init + ' ' + player_name + ' ' + player_arclass
        iniciative_order = iniciative_order + [player_data]

    list_iniciative = sorted(iniciative_order, reverse = True)
    iniciative_num = len(list_iniciative)
    for index in range(0, iniciative_num):
        print()
        print(str(index+1) + ')', list_iniciative[index])

def main():
    while True:
        print()
        print('1) Create a new Monster')
        print('2) Delete a Monster')
        print('3) Show Monster Stats')
        print('4) Initiative Tracker')
        print()
        menu = input('Choose one option(0 to Exit): ')
        if menu == '1':
            new_monster()
        if menu == '2':
            delete_monster()
        if menu == '3':
            show_monster_menu()
        if menu == '4':
            iniciative()
        if menu == '0':
            break
main()
