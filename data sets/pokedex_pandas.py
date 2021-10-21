#!/usr/bin/env python3
  
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    poke_df = pd.read_csv("pokedex.txt", index_col=1)
    poke_df.drop_duplicates(inplace=True)
    poke_df.drop(poke_df.columns.difference(['Name','Type 1','Type 2','Attack']), 1, inplace=True)
    sorted_by_attack = poke_df.sort_values(["Attack"], ascending=False)
    #sorted_by_attack.set_index("Name")

    print(sorted_by_attack.head(10))

    sorted_by_attack.head(10).plot(kind="barh")
    plt.savefig("/home/student/static/attackers.png", bbox_inches='tight')

if __name__ == "__main__":
    main()
