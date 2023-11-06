class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            return len(state) <= len(nums)

        def get_candidates(state):
            if not state:
                return nums
            else:
               return [num for num in nums if num > max(state)]

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(tuple(state.copy()))
                # return

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        solutions = []
        state = set()
        search(state, solutions)
        return solutions
