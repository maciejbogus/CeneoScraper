import os
import pandas as pd
import matplotlib.pyplot as plt

print("\nLista dostępnych opinii:")
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_id = input("\nPodaj id produktu: ")

opinions = pd.read_json(f"opinions/{product_id}.json")
print(opinions)


opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",", ".")))
opinions_count = len(opinions.index)
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
avarage_score = opinions.stars.mean().round(2)

recommendation = opinions.recomendation.value_counts(dropna = False)
recommendation.plot.pie(
    label="", 
    autopct="%1.1f%%", 
    colors=["green", "blue", "red"]
)
plt.title("Rekomendacja")
plt.savefig(f"plots/{product_id}_recomendations.png")
plt.close()

stars = opinions.stars.value_counts()
stars.plot.bar()
plt.title("Ocenty produktów")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.grid(True)
plt.xticks(rotation=0)
plt.show()

print(recommendation)