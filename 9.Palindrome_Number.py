class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False

        string = str(x)
        if string == string[::-1]:
            return True
        else:
            return False

#Palindrome：回文
#前から読んでも後ろから読んでも同じ数字をTrue、その他をFalseとする
#xが-の時は必ずfalse、+のときはxの中身を逆転させる