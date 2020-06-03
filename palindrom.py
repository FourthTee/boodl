#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#Example 1 Input: 121 Output: true
#Example 2 Input: 121 Output: false Explanation: From left to right, it reads 121. From right to left, it becomes 121. Therefore it is not a palindrome.
#Example 3 Input: 10 Output: false Explanation : Reads 01 from right to left. Therefore it is not a palindrome.

def palindrom(n):

    rev_n = reverse(n)
    if rev_n == n:
        return True
    else:
        return False

# Helper function to reverse the number
def reverse(num):
    new_num = 0
    while num > 0:
        last = num % 10
        new_num = new_num * 10 + last
        num = num//10
    return new_num

