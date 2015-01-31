import collections

class Card:
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    def __init__(self, cardstring):
        self.facevalue, self.suit = Card.values[cardstring[0]], cardstring[1]
            
class PokerHand:
    # basically 9 types of hands
    hands = {"high_card": 0, "one_pair": 1, "two_pair": 2, "three_kind": 3,
             "straight": 4, "flush": 5, "full_house": 6, "four_kind": 7,
             "straight_flush": 8}
    def __init__(self, cards):
        self.cards = sorted(cards, key=lambda x: x.facevalue)

    def is_flush(self):
        """Returns true if this hand is a flush"""
        return sum([True for i in range(1, 5) if self.cards[0].suit ==
                self.cards[i].suit]) == 4
    
    def is_straight(self):
        """Returns True if it's a straight"""
        streak = 1
        for i, card in enumerate(self.cards):
            if i == len(self.cards) - 1:
                continue
            if card.facevalue + 1 == self.cards[i + 1].facevalue:
                streak += 1
        if streak == 5:
            return True
        if (streak == 4 and self.cards[0].facevalue == 2 and
                self.cards[3].facevalue == 5 and self.cards[4] == 14):
            return True
        return False
    
    def get_best_set(self):
        """returns rank of the hand from hands 0 to 8"""
        uniques = collections.Counter([card.facevalue for card in
            self.cards]).most_common()
        if uniques[0][1] == 4:
            return 7
        elif uniques[0][1] == 3:
            if uniques[1][1] == 2:
                return 6
            else:
                return 3
        elif uniques[0][1] == 2:
            if uniques[1][1] == 2:
                return 2
            else:
                return 1
        return 0

    def get_hand(self):
        flush = self.is_flush()
        straight = self.is_straight()
        best = max(int(flush) * 6, int(straight) * 5, int(straight and flush) *
                   8)
        best = max(self.get_best_set(), best)
        return best

    def compare_sets(self, other):
        these_most_common = sorted(collections.Counter([card.facevalue for card in
            self.cards]).most_common(), key=lambda x: x[1] * 100 + x[0])
        other_most_common = sorted(collections.Counter([card.facevalue for card in
            other.cards]).most_common(), key=lambda x: x[1] * 100 + x[0])
        i = -1
        while these_most_common[i][0] == other_most_common[i][0]:
            i -= 1
        return these_most_common[i][0] > other_most_common[i][0]
        

    def compare_straights(self, other):
        return (self.cards[-1].facevalue > other.cards[-1].facevalue and
                self.cards[0].facevalue > other.cards[0].facevalue)
        
    def compare(self, other):
        this_hand = self.get_hand()
        other_hand = other.get_hand()
        if this_hand == other_hand:
            if this_hand == PokerHand.hands["straight"]:
                return self.compare_straights(other)
            else:
                return self.compare_sets(other)
        else:
            return this_hand > other_hand


with open("p054_poker.txt", "rb") as hands:
    count = 0
    for cards in hands:
        cards = cards.strip().split(" ")
        first_hand = PokerHand([Card(c) for c in cards[:5]])
        second_hand = PokerHand([Card(c) for c in cards[5:]])
        count += int(first_hand.compare(second_hand))
print count
