from collections import Counter

from collections import Counter, defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_str = "balloon"
        check_lst = list()
        ans = 0

        if set(balloon_str) <= set(text):
            balloon_cnt = dict(Counter(balloon_str))
            text_cnt = dict(Counter(text))

            for key, value in balloon_cnt.items():  # if we iterate text_cnt, maybe there are alphabets not in "balloon"
                check_lst.append(int(text_cnt[key] / value))
            ans = min(check_lst)

        return ans


class Solution:
    """Time taken
    00 : 12 : 23
    """
    def maxNumberOfBalloons(self, text: str) -> int:
        set_balloon = set(list("balloon"))
        set_text = set(list(text))
        if set_balloon.intersection(set_text) == set_balloon:
            c_dict_ballon = dict(Counter(list("balloon")))
            c_dict_text = dict(Counter(list(text)))
            num_lst = list()
            for k, v in c_dict_ballon.items():
                num_lst.append(c_dict_text[k] // v)
            return min(num_lst)
        else:
            return 0
