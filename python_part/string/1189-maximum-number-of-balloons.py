from collections import Counter


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
