from backend.calculate_result import calculate_result
from backend.runoff import calculate_runoff

if __name__ == '__main__':
    candidates = ['md', 'ls', 'dt', 'bj']
    # preferences, first number is index of highest preferred candidate
    test_votes = [('md', 'ls', 'dt', 'bj'), ( 'md', 'bj', 'dt','ls'), ('ls', 'dt', 'md', 'bj'), ('ls', 'dt', 'bj', 'md'), ('md', 'bj', 'dt', 'ls'), ('dt', 'md', 'ls', 'bj'), ('dt', 'md', 'bj', 'ls'), ('dt', 'ls', 'md', 'bj'), ('md', 'ls', 'dt', 'bj'), ('dt', 'bj', 'md', 'ls'), ('dt', 'bj', 'ls', 'md'), ('bj', 'ls', 'md', 'dt'), ('bj', 'ls', 'dt', 'md'), ('bj', 'dt', 'md', 'ls'), ('bj', 'dt', 'ls', 'md')]
    winner = calculate_runoff(test_votes, candidates)
    print(winner)