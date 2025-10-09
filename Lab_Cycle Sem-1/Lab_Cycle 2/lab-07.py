import pandas as pd

data = {
    "SN": [1, 2, 3, 4, 5],
    "Name": ["Geoffrey Hinton",
             "Yann LeCun",
             "Andrew Ng",
             "Phila Suoni",
             "Yemehi Yathi"
    ],
    "Country": ["Canada","France","USA","UK","France"],
    "Innovation": ["Deep Learning",
                   "Convolutional Neural Nets",
                   "Online ML Courses",
                   "Artificial Intelligence",
                   "Data Analytics"
    ],
    "Year": [1986, 1989, 2011, 2023, 2025],
}

df=pd.DataFrame(data)
df.to_csv("tech_innovators.csv",index=False)

df_loader=pd.read_csv("tech_innovators.csv")
filtered=df_loader[df_loader["Year"]>=2000]

print("Innovators who contributed before the year 2000:\n")
print(filtered[["Name", "Country", "Innovation", "Year"]])