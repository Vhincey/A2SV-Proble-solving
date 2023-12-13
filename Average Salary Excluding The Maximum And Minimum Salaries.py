class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        min_salary = min(salary)
        max_salary = max(salary)

        #total_salary = 0
        salary.sort()
        salary = salary[1 : -1] 

        total_salary = sum(salary) 
        average_salary = float(total_salary) / len(salary)
        return average_salary
