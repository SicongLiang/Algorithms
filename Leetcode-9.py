class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 当 x < 0 时，x 不是回文数。
        # 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # 则其第一位数字也应该是 0，只有 0 满足这一属性
        # 即：特殊情况，x<0都不是回文；末尾是0的大于0的数也都不是回文
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        revertNum = 0
        while x > revertNum:
            y = x % 10 # 最低位数字，除以10取余数获得
            revertNum = revertNum * 10 + y # 每次添加y到末尾，前面的数往前移一位，即乘10
            x //= 10 # 移掉一位自己要除以10
                
        # 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        # 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        # 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return (x == revertNum or x == revertNum // 10)
        
        # 翻转法：翻转后半段数字来判断是否是回文
        # 时间复杂度：O(logn)，空间复杂度：O(1)
        # 第二个想法是将数字本身反转，然后将反转后的数字与原始数字进行比较，如果它们是相同的，那么这个数字就是回文。
        # 但是，如果反转后的数字大于 int.MAX，我们将遇到整数溢出问题。
        # 按照第二个想法，为了避免数字反转可能导致的溢出问题，为什么不考虑只反转 int 数字的一半？毕竟，如果该数字是回文，其后半部分反转后应该与原始数字的前半部分相同

        