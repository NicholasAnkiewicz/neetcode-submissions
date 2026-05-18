class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people, reverse=True)
        print(people)
        total = 0
        i = 0
        j = len(people)-1
        while i <= j:
            if people[i] + people[j] <= limit:
                total += 1
                i += 1                    
                j -= 1
            else:
                i += 1
                total += 1
            print("Total: " + str(total) + " i = " + str(i) + " j = " + str(j))
        return total