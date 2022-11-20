import argparse
import csv
import pandas as pd
import random

# csvをデッキリストに変換する
def create_library(df):
    library = []
    for x in df.itertuples():
        for _ in range(x.amount):
            library.append(x.card_name)

    return library


# デッキリストからカードを1枚引く
def draw_card(library):
    pass


def deck_play(args):
    deck = args.deck
    df = pd.read_csv(deck, delimiter=' ', header=0)
    # デッキリストを成形
    library = create_library(df)
    # デッキリストの順番をrandomに変更する
    random.shuffle(library)
    print(library)
    draw_card(library)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--deck', type=str, default='sample_deck.csv')
    args = parser.parse_args()

    deck_play(args)


if __name__ == '__main__':
    main()