import random

class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def __str__(self):
        return 'Vu khi: {} - Sat thuong : {}'.format(self.name, self.damage)
weapon_list = [
    Weapon('Bua', 100),
    Weapon('Dao', 120),
    Weapon('Keo', 90),
    Weapon('Xa mau', 110),
    Weapon('Xeng', 200)
]
    
class Fighter():
    def __init__(self, name, hp, weapon_list):  # nhap vao nguoi choi va Tui_Vu_khi
        self.name = name
        self.hp = hp
        self.weapon_list = weapon_list
        self.weapon = ''   # Tam thoi khoi tao vukhi = ''
        
    def __str__(self):
        return 'Nguoi choi {} - Mau {} '.format(self.name, self.hp)
    
    def lay_vu_khi(self):
        self.weapon = random.choice(self.weapon_list)
    
    def strike(self, opponent):
        opponent.hp = opponent.hp - self.weapon.damage
        
    def win(self):
        print('The WInner is : {} '.format(self.name))
        print('HP remain is : {}'.format(self.hp))
    
    def is_alive(self):
        return self.hp > 0
    
def solve(player1, player2):
    turn_select = random.choice(range(2))
    print('Tran chien bat dau')
    print('{}'.format(player1))
    print('{}'.format(player2))
    
    while player1.is_alive() and player2.is_alive():
        player1.lay_vu_khi()
        player2.lay_vu_khi()
        print('Round {} : {} with {} vs {} with {} '
              .format(turn_select, player1, player1.weapon,
                     player2, player2.weapon))
        if turn_select % 2 == 0:
            player1.strike(player2)
        else:
            player2.strike(player1)
            
        turn_select += 1
        
    if player1.is_alive is not True:
        result = player2.win()
    else:
        result = player1.win()
    
    return result

def main():
    player1 = Fighter('Chuong', 1000, weapon_list)
    player2 = Fighter('Nguyen', 1100, weapon_list)
    print(solve(player1, player2))
    
    
if __name__ == "__main__":
    main()
	
	
# Tran chien bat dau
# Nguoi choi Chuong - Mau 1000 
# Nguoi choi Nguyen - Mau 1100 
# Round 0 : Nguoi choi Chuong - Mau 1000  with Vu khi: Bua - Sat thuong : 100 vs Nguoi choi Nguyen - Mau 1100  with Vu khi: Keo - Sat thuong : 90 	





