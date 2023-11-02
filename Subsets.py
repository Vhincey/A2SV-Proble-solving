 def is_valid_state(state):
            if len(state) <= len(nums):
                return True

        def get_candidates(state):
            lst = []
            if not state:
                return nums
            else:
                lst = [num for num in nums if num > max(state)]
            return lst

        def search(state, solutions):
            if is_valid_state(state):
                solutions.add(tuple(state.copy()))
                # return

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        solutions = set()
        state = set()
        search(state, solutions)
        return solutions
