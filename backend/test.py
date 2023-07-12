from db.db import Database
from runoff import calculate_runoff
from fptp import calculate_ftpt

if __name__ == '__main__':
    print('Testing runoff')
    candidates = ['Modi', 'Laxman Singh', 'Donald Trump', 'Boris Johnson']
    res = calculate_runoff([(0,3,1,2), (2,1,3,0), (1,0,2,3), (2,1,3,0), (0,3,1,2), (0,1,2,3)], candidates)
    print(res)
    res2 = calculate_ftpt([0,0,0,0,0,0,0,2,3,1,2,2,2,3,1,2,2,3,0,2,1,1,1,1], candidates)
    print(res2)
    assert res == 'Modi'
    assert res2 == ['Modi']
    # db = Database()
    # db.connect()
