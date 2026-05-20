class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num]:
                for j in range(num, num + groupSize):
                    if not count[j]:
                        return False
                    count[j] -= 1

        return True