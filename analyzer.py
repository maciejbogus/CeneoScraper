import os
import pandas as pd

print("\nLista dostępnych opinii:")
print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_id = input("\nPodaj id produktu: ")

opinions = pd.read_json(f"opinions/{product_id}.json")
print(opinions)