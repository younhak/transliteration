import re

BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 00 - 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
CHOSUNG_MAP = ['g', 'kk', 'n', 'd', 'tt', 'r', 'm', 'b', 'pp', 's', 'ss', '', 'j', 'jj', 'ch',' k', 't', 'p', 'h', 'l']

# 00 - 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JUNGSUNG_MAP = ['a', 'ae', 'ya', 'yae', 'eo', 'e', 'yeo', 'ye', 'o', 'wa', 'wae', 'oe', 'yo', 'u', 'wo', 'we', 'wi', 'yu', 'eu', 'ui', 'i']

# 00 - 27 + 1 (1 is None)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JONGSUNG_MAP = ['', 'k', 'k', 'k', 'n', 'n', 'n', 't', 'l', 'k', 'm', 'p', 't', 't', 'p', 'l', 'm', 'p', 'p', 't', 't', 'ng', 't', 't', 'k', 't', 'p', '']

def split_kor(kor_word):
    holder = []
    for c in list(kor_word):
        if '가' <= c <= '힣':
            chosung = (ord(c) - ord('가')) // CHOSUNG
            jungsung = ((ord(c) - ord('가')) - CHOSUNG * chosung) // JUNGSUNG
            jongsung = (ord(c) - ord('가')) - CHOSUNG * chosung - JUNGSUNG * jungsung

            holder.append(CHOSUNG_MAP[chosung])
            holder.append(JUNGSUNG_MAP[jungsung])
            holder.append(JONGSUNG_MAP[jongsung])
            holder.append("-")

            # res.append([CHOSUNG_MAP[chosung], JUNGSUNG_MAP[jungsung], JONGSUNG_MAP[jongsung]])
        else:
            holder.append(c)

        res = "".join(holder)
    return res


split_kor('집에 가지마')
