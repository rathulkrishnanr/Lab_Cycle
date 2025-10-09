import pandas as pd

data ={
    "SN":[1, 2,3 ],
    "Name":["Linus Torvalds",
            "Tim Berners-Lee",
            "Guido van Rossum"],
    "Country":["Finland",
               "England",
               "Netherlands"],
    "Contribution":["Linux",
                    "World wide Web",
                    "Python"],
    "Year":[1991,1990,1991]
}

df = pd.DataFrame(data)
df.to_csv("contributors.csv", index= False)

print("Data written to contributors.csv")