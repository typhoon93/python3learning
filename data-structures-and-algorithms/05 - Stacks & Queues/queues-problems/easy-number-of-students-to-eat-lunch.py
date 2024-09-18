"""


The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.



Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3


Constraints:

1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.
"""
import collections


class Solution(object):
    # def countStudents(self, students, sandwiches):
    #     """
    #     My solution.
    #     SC = O(n)
    #     TC = O(n)
    #     :type students: List[int]
    #     :type sandwiches: List[int]
    #     :rtype: int
    #     """
    #     students = collections.deque(students)
    #     sandwiches = collections.deque(sandwiches)
    #     loops = 0
    #     while sandwiches:
    #         if loops >= len(students): #detects loops
    #             break
    #         if students[0] == sandwiches[0]:
    #             students.popleft()
    #             sandwiches.popleft()
    #             loops = 0
    #         else:
    #             students.append(students.popleft())
    #             loops += 1
    #     return len(students)

    def countStudents(self, students, sandwiches):
        """
        Optimized solution GPT
        SC = O(1)
        TC = O(n)
        """
        count = [students.count(0), students.count(1)] # this is a count of students and the type of sandwich they prefer.
        # since sandwiches is a stack (reverse stack due to exercise details)
        # only the last element (first due to being reverse stack) can be eaten at any given time.
        # so if there are no students taht will eat it (count[s] == 0) -> well then
        # the remaining students will loop into perpetuity, since no one will take the top sandwich
        for s in sandwiches:
            if count[s]:
                count[s] -= 1
            else: # No students prefer this sandwich, break early.
                break

        # The remaining students who couldn't eat.
        return sum(count)

sol = Solution()
students = [1,1,1,0,0,1]; sandwiches = [1,0,0,0,1,1];
print(sol.countStudents(students, sandwiches))