from itertools import permutations


def solve_crypto():
    lett = 'SENDMORY'

    for a in permutations(range(10), len(lett)):
        map1 = dict(zip(lett, a))
        if map1['S'] == 0 or map1['M'] == 0:
            continue

        send = map1['S'] * 1000 + map1['E'] * 100 + map1['N'] * 10 + map1['D']
        more = map1['M'] * 1000 + map1['O'] * 100 + map1['R'] * 10 + map1['E']
        money = map1['M'] * 10000 + map1['O'] * 1000 + map1['N'] * 100 + map1['E'] * 10 + map1['Y']

        if send + more == money:
            return map1


sol = solve_crypto()
if sol:
    print("Solution found!")
    for letters, digits in sol.items():
        print(f"{letters} = {digits}")
else:
    print("Solution not found!")
