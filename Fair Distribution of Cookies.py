class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # state = [0] * k
        # ans = sum(cookies)

        # def search(state, idx):
        #     nonlocal ans  # To declare 'ans' as a nonlocal variable
        #     if idx >= len(cookies):
        #         ans = min(ans, max(state))
        #         return

        #     for i in range(k):
        #         state[i] += cookies[idx]
        #         if state[i] < ans:
        #             search(state, idx + 1)
        #         state[i] -= cookies[idx]

        # search(state, 0)
        # return ans

        state = [0] * k
        ans = sum(cookies)
        
        def search(state, idx):
            nonlocal ans
            if idx == k:
                if sum(cookies) == 0:
                    ans = min(ans, max(state))
                return
            
            for i in range(len(cookies)):
                if cookies[i] == 0:
                    continue
                state[idx] += cookies[i]
                temp = cookies[i]
                cookies[i] = 0

                if state[idx] < ans:
                    search(state, idx)
                    search(state, idx+1)

                state[idx] -= temp
                cookies[i] = temp

        search(state, 0)
        return ans

