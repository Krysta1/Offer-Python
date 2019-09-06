class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < len(s) and s[i] == ' ': i += 1
        while j > 0 and s[j] == ' ': j -= 1
        if i > j: return False
        sub_s = s[i: j - i + 1]

        if sub_s[0] == '-' or sub_s[0] == '+':
            sub_s = sub_s[1:]

        if sub_s is None or sub_s == '.':
            return False

        i, dot_count, e_count = 0, 0, 0
        while i < len(sub_s):
            if '0' <= sub_s[i] <= '9':
                i += 1
                # continue

            elif sub_s[i] == '.':
                dot_count += 1
                if dot_count > 1 or e_count >= 1:
                    return False
                i += 1

            elif sub_s[i] == 'e' or sub_s[i] == 'E':

                e_count += 1
                if i + 1 == len(sub_s) or not i or e_count > 1 or i == 1 and sub_s[0] == '.':
                    return False
                if sub_s[i + 1] == '-' or sub_s[i + 1] == '+':
                    if i + 2 == len(sub_s):
                        return False
                    i += 1
                i += 1

            else:
                return False

        return True