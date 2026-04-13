import json
import os


# filename = 'stats.json'

def open_file(filename):
    if not os.path.exists(filename):
        initial_data = {'total_kills': 0, 'total_deaths': 0, 'win_rate': 0, 'kd': 0, 'current_win_streak': 0,
                        'last_matches': '', 'total_matches': 0, 'total_wins': 0, 'last_match_kd': 0, 'last_matches_kd': ''}
        with open(filename, 'w') as f:
            json.dump(initial_data, f)
        return initial_data
    with open(filename, 'r') as f:
        return json.load(f)


def save_file(filename, current_data):
    with open(filename, 'w') as f:
        json.dump(current_data, f, indent=4)


def calculate_kd(kills, deaths):
    if deaths == 0:
        return float(kills)
    return round(kills / deaths, 2)


def get_stats():
    try:
        k = int(input('Киллов за матч: '))
        d = int(input('Смертей за матч: '))
        return k, d
    except ValueError as e:
        print('Вводи число')


def calculate_win_rate(all_matches, wins):
    res = (wins / all_matches) * 100
    return round(res, 1)


def get_win_stats():
    try:
        m = int(input('Всего матчей: '))
        w = int(input('Побед: '))
        return m, w
    except ValueError:
        print('вводи только целые числа')


def find_win_streak(l):
    counter = 0
    current_streak = 0
    for i in l:
        if i == 'W':
            counter += 1
            if counter > current_streak:
                current_streak = counter
        else:
            counter = 0

    return current_streak


def get_results():
    last_matches_results = input('Результаты ласт матчей: ').split()
    return last_matches_results


def main():
    data = open_file('stats.json')
    stats = get_stats()
    results = get_results()
    kill, death = stats
    data['total_kills'] += kill
    data['total_deaths'] += death
    rate = calculate_kd(data['total_kills'], data['total_deaths'])
    last_match_kd = calculate_kd(kill, death)
    data['kd'] = rate
    data['last_match_kd'] = last_match_kd
    if not data['last_matches_kd']:
        data['last_matches_kd'] += str(last_match_kd)
    else:
        data['last_matches_kd'] += ', ' + str(last_match_kd)
    win_stats = get_win_stats()
    matches, win = win_stats
    data['total_matches'] += matches
    data['total_wins'] += win
    data['win_rate'] = calculate_win_rate(data['total_matches'], data['total_wins'])
    data['last_matches'] += ' ' + ' '.join(results)
    full_history = data['last_matches'].split()
    data["current_win_streak"] = find_win_streak(full_history)
    save_file('stats.json', data)
    print('даннве сохраненф')

if __name__ == '__main__':
    while True:
        print('1. Добавить')
        print('2. Выйти')
        inp = int(input('Выбор: '))
        if inp == 1:
            main()
        if inp == 2:
            break