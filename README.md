# Korean Character Romanization
Romanized the Korean to English

This is not perfect for Korean pronunciation because the phonological process is not reflected.



## Characteristic of Korean Character

![hanguel](https://user-images.githubusercontent.com/40286691/54249090-48be3200-4582-11e9-962e-6259641d5bbf.png)

### Onset

| KOREAN(onset) | ROMAN |
| ------------- | ----- |
| ㄱ            | g     |
| ㄲ            | kk    |
| ㄴ            | n     |
| ㄷ            | d     |
| ㄸ            | tt    |
| ㄹ            | r     |
| ㅁ            | m     |
| ㅂ            | b     |
| ㅃ            | pp    |
| ㅅ            | s     |
| ㅆ            | ss    |
| ㅇ            |       |
| ㅈ            | j     |
| ㅉ            | jj    |
| ㅊ            | ch    |
| ㅋ            | k     |
| ㅌ            | t     |
| ㅍ            | p     |
| ㅎ            | h     |

### Nucleus

| KOREAN(Nucleus) | ROMAN |
| --------------- | ----- |
| ㅏ              | a     |
| ㅐ              | ae    |
| ㅑ              | ya    |
| ㅒ              | yae   |
| ㅓ              | eo    |
| ㅔ              | e     |
| ㅕ              | yeo   |
| ㅖ              | ye    |
| ㅗ              | o     |
| ㅘ              | wa    |
| ㅙ              | wae   |
| ㅚ              | oe    |
| ㅛ              | yo    |
| ㅜ              | u     |
| ㅝ              | wo    |
| ㅞ              | we    |
| ㅟ              | wi    |
| ㅠ              | yu    |
| ㅡ              | eu    |
| ㅢ              | ui    |
| ㅣ              | i     |

### Coda

| KOREAN(Coda) | ROMAN |
| ------------ | ----- |
|              |       |
| ㄱ           | k     |
| ㄲ           | k     |
| ㄳ           | k     |
| ㄴ           | n     |
| ㄵ           | n     |
| ㄶ           | n     |
| ㄷ           | t     |
| ㅌ           | l     |
| ㄺ           | k     |
| ㄻ           | m     |
| ㄼ           | p     |
| ㄽ           | t     |
| ㄾ           | t     |
| ㄿ           | p     |
| ㅀ           | l     |
| ㅁ           | m     |
| ㅂ           | p     |
| ㅄ           | p     |
| ㅅ           | t     |
| ㅆ           | t     |
| ㅇ           | ng    |
| ㅈ           | t     |
| ㅊ           | t     |
| ㅋ           | k     |
| ㅌ           | t     |
| ㅍ           | p     |
| ㅎ           |       |



## Usage

```python
import pandas as pd
from kor2eng import kor_romanizied

from dask import dataframe as dd
from dask.multiprocessing import get
from multiprocessing import cpu_count

# Import data set --------------------------------------------------
korean_words = pd.DataFrame({"KOREAN": ["안녕하세요",
                                        "감사합니다",
                                        "반갑습니다"],
                             "MEANING": ["Hi",
                                         "Thank you",
                                         "Nice to meet you"]})

# Romanized --------------------------------------------------------
nCores = cpu_count()
romanized_string = dd.from_pandas(korean_words, npartitions=nCores).\
   map_partitions(
      lambda df : df.apply(
         lambda x : kor_romanizied.split_kor(x.KOREAN), axis=1)).\
   compute(scheduler='processes')

korean_words["ROMANIZED"] = romanized_string

print(korean_words)
#   KOREAN           MEANING            ROMANIZED
# 0  안녕하세요                Hi  an-nyeong-ha-se-yo-
# 1  감사합니다         Thank you    gam-sa-hap-ni-da-
# 2  반갑습니다  Nice to meet you  ban-gap-seup-ni-da-
```

