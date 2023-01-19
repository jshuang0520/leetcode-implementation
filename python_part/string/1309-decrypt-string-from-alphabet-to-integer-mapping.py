import string
from collections import defaultdict


class Solution:
    def freqAlphabets(self, s: str) -> str:
        """
        since there's #, so we deal with this string "backward"
        """
        ans_str = ''
        dd = defaultdict(str)

        for idx, alphabet in enumerate(list(string.ascii_lowercase), 1):  # enumerate(..., 1) means enumerate from 1
            dd[str(idx)] = alphabet

        while len(s) > 0:
            # print(f'original string: {s}')
            if s[-1] == '#':
                ans_str = dd[s[-3:-1]] + ans_str
                s = s[:-3]  # update the string
                # print(f'new string: {s[:-3]}, ans_str: {ans_str}')
            else:
                ans_str = dd[s[-1]] + ans_str
                s = s[:-1]  # update the string
                # print(f'new string: {s[:-1]}, ans_str: {ans_str}')
            # print('--')
        return ans_str
print(Solution.freqAlphabets(None, s="10#11#12"))


class Solution:
    """Time taken
    01 : 09 : 20
    """
    def freqAlphabets(self, s: str) -> str:
        res_lst = list()
        # {num: alphabet} mapping dictionary
        values = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        keys = range(1, len(values) + 1)
        map_dict = dict(zip(keys, values))

        # chunk, backward
        while len(s) > 0:
            # if "#" in s[-3::]:  # ValueError '#1'
            if s[-3::].endswith("#"):
                res_lst.insert(0, map_dict[int(s[-3:-1:])])
                s = s[:-3]
                # print('check1:', s)
            else:
                res_lst.insert(0, map_dict[int(s[-1::])])
                s = s[:-1]
                # print('check2:', s)
        return "".join(res_lst)

# # FIXME: (1) "10#11#12", Output "b", Expected "jkab"; (2) "1326#", Output "z", Expected "acz"
# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         res_lst = list()
#         # {num: alphabet} mapping dictionary
#         values = [chr(x) for x in range(ord('a'), ord('z')+1)]
#         keys = range(1, len(values)+1)
#         map_dict = dict(zip(keys, values))

#         # chunk, backward
#         while len(s) > 0:
#             # if "#" in s[-3::]:  # ValueError '#1'
#             if ("#" in s[-3::]) and (s[-3::].endswith("#")):
#                 res_lst.insert(0, map_dict[int(s[-3:-1:])])
#                 s = s[:-3]
#             else:
#                 res_lst.insert(0, map_dict[int(s[-1::])])
#                 s = s[:-1]
#             return "".join(res_lst)


# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         res_lst = list()
#         # {num: alphabet} mapping dictionary
#         values = [chr(x) for x in range(ord('a'), ord('z')+1)]
#         keys = range(1, len(values)+1)
#         map_dict = dict(zip(keys, values))

#         lst = list()  # pound_sign_idx_lst
#         for i, c in enumerate(s):
#             if "#" == c:
#                 lst.append(i)


# # FIXME: (1) "10#11#12", Output "jkl", Expected "jkab"; (2) "1326#", Output "acbf", Expected "acz"
# class Solution:
#     def freqAlphabets(self, s: str) -> str:
#         res_lst = list()
#         # {num: alphabet} mapping dictionary
#         values = [chr(x) for x in range(ord('a'), ord('z')+1)]
#         keys = range(1, len(values)+1)
#         map_dict = dict(zip(keys, values))

#         s_lst = [x for x in s.split("#")]
#         for word in s_lst:
#             if len(word) == 2:
#                 res_lst.append(map_dict[int(word)])
#             else:
#                 for i in range(0, len(word)):
#                     res_lst.append(map_dict[int(word[i])])
#         return "".join(res_lst)
