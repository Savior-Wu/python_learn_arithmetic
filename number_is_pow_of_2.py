#! /usr/bin/python
#! -*- coding:utf-8 -*-

import random

'''
def nfromm(m, n, unique=True):
    """
    从[0, m)中产生n个随机数
    :param m:
    :param n:
    :param unique:
    :return:
    """
    if unique:
        box = [i for i in range(m)]
        out = []
        for i in range(n):
            index = random.randint(0, m - i - 1)

            # 将选中的元素插入的输出结果列表中
            out.append(box[index])

            # 元素交换，将选中的元素换到最后，然后在前面的元素中继续进行随机选择。
            box[index], box[m - i - 1] = box[m - i - 1], box[index]
        return out
    else:
        # 允许重复
        out = []
        for _ in range(n):
            out.append(random.randint(0, m - 1))
        return out

# nfromm(10,8)
'''
'''
从正整数 N 开始，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false

此方法并没有进行随机排序（只进行升序、降序），只是从2的幂入手，计算最小数字和最大数字的二进制位数，然后生成二进制位数区间

计算结果列表并降序排列，如果与N降序符合，则返回True，否则False
'''
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        #数字N转化为字符串，然后转为列表，升降序排列
        tmp = str(N)
        tmp_list = list(tmp)
        tmp_list.sort(reverse=True)
        tmp_list1 = list(tmp)
        tmp_list1.sort()
        # print(tmp_list)
        # print(tmp_list1)

        #如果列表第一位为0，则与最近的非0数交换，得到最小数字，返回最大数字和最小数字的最高二进制位
        def list_to_bin(tmp):
            for i in range(len(tmp)):
                if tmp[i] != '0' and 0 < i < len(tmp) - 1 and tmp[0] == '0':
                    tmp[0], tmp[i] = tmp[i], tmp[0]
                if tmp[0] != '0':
                    break

            tmp_bin = bin(int(str("".join(tmp))))
            # print(tmp_bin)
            #减去'0b'两个字符位，二进制位从0开始，再减1，得到最小/最大的二进制位
            tmp_len = len(str(tmp_bin)) - 3
            return tmp_len

        min_len = list_to_bin(tmp_list1)
        max_len = list_to_bin(tmp_list)
        bin_list = []
        # print(min_len,max_len)

        #计算二进制数列表
        # 获得最小/最大二进制位后，最大位再多计算一位，我也不知道自己为啥这样做，可能是为了安心吧(:
        for i in range(min_len, max_len + 2):
            bin_str = list(str(int(2 ** i)))
            bin_str.sort(reverse=True)
            bin_list.append(str("".join(bin_str)))
        # print(bin_list)

        #比较降序排列的二进制列表中，是否有数和原降序排数N一致，如果一致，则返回TRUE，否则FALSE
        Flag = False
        for i in bin_list:
            if i == str("".join(tmp_list)):
                Flag = True
                break
        if Flag:
            return True
        else:
            return False

if __name__=="__main__":
    c=Solution()
    c.reorderedPowerOf2(2014)
