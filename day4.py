import sys
import numpy as np
import pandas as pd

df = pd.DataFrame()

dic = {}
for line in sys.stdin:
    if (line == '\n'):
        df = df.append(dic, ignore_index=True)
        dic = {}
    else:
        fields = line.split()
        for item in fields:
            dic.update({item.split(":")[0]: item.split(":")[1]})

df = df.drop(columns = "cid", axis = 1)
df = df.dropna()
print(len(df))

df["byr"] = df["byr"].astype(int)
df = df[df["byr"] <= 2002]
df = df[df["byr"] >= 1920]

df["iyr"] = df["iyr"].astype(int)
df = df[df["iyr"] <= 2020]
df = df[df["iyr"] >= 2010]

df["eyr"] = df["eyr"].astype(int)
df = df[df["eyr"] <= 2030]
df = df[df["eyr"] >= 2020]

df = df[df["hcl"].str.contains("#[0-9a-f]{6}")]

eyecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
df = df[df["ecl"].isin(eyecl)]

df = df[df["pid"].str. contains("\d{9}")]
df = df[df["pid"].str.len() == 9]

df = df.reset_index().drop(columns = "index")
for index, row in df.iterrows():
    hgt = row["hgt"]
    if (hgt[-2:] == "cm" and len(hgt) == 5):
        if (not (150 <= int(hgt[0:3]) <= 193)):
            df = df.drop(index=index)
    elif (hgt[-2:] == "in" and len(hgt) == 4):
        if (not (59 <= int(hgt[0:2]) <= 76)):
            df = df.drop(index = index)
    else:
        df = df.drop(index=index)

print(df.head())
print(len(df))
