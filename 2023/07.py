from functools import cmp_to_key

lines = open("input/07.txt").read().splitlines()
lines = [line.split() for line in lines]


def get_hand_type(hand, Jrule=False):
    unique = {c: hand.count(c) for c in set(hand)}
    if Jrule and "J" in unique and len(unique) > 1:
        Jcount = unique.pop("J")
        unique[max(unique, key=unique.get)] += Jcount
    if len(unique) == 1:
        return 7  # Five of a kind
    if len(unique) == 2 and 4 in unique.values():
        return 6  # Four of a kind
    if len(unique) == 2 and 3 in unique.values():
        return 5  # Full house
    if len(unique) == 3 and 3 in unique.values():
        return 4  # Three of a kind
    if len(unique) == 3 and 2 in unique.values():
        return 3  # Two pair
    if len(unique) == 4 and 2 in unique.values():
        return 2  # One pair
    if len(unique) == 5:
        return 1  # High card


def cmp(a, b, Jrule=False):
    type_a, type_b = get_hand_type(a, Jrule), get_hand_type(b, Jrule)
    if type_a != type_b:
        return type_a - type_b
    card_rank = "23456789TJQKA"
    if Jrule:
        card_rank = "J23456789TQKA"
    for i in range(len(a)):
        if card_rank.index(a[i]) != card_rank.index(b[i]):
            return card_rank.index(a[i]) - card_rank.index(b[i])
    return 0


# part one
lines.sort(key=lambda x: cmp_to_key(cmp)(x[0]))
print(sum((i + 1) * int(line[1]) for i, line in enumerate(lines)))

# part two
lines.sort(key=lambda x: cmp_to_key(lambda a, b: cmp(a, b, True))(x[0]))
print(sum((i + 1) * int(line[1]) for i, line in enumerate(lines)))
