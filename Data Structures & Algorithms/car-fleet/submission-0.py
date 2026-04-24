class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(0, len(position)):
            pairs.append([position[i],speed[i]])
        stack = []
        for pair in sorted(pairs, reverse=True):
            t_to_des = (target - pair[0])/pair[1]
            if len(stack) != 0:
                if stack[-1][1] >= t_to_des:
                    continue
                else:
                    stack.append([pair, t_to_des])
            else:
                stack.append([pair, t_to_des])
        return len(stack)