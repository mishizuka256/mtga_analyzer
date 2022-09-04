import argparse
import csv
import pandas as pd

# csvをデッキリストに変換する
def create_deck(deck_df):
    deck_list = []
    for index, row in deck_df.iterrows():
        # ここにカード枚数分をリストにappendする
        import pdb; pdb.set_trace()
    
    return deck_list

# デッキリストの順番をrandomに変更する
def shuffle_deck(deck_list):
    pass

# デッキリストからカードを1枚引く
def draw_card(deck_list):
    pass


def deck_play(args):
    deck = args.deck

    # with open(deck, 'r') as f:
    #     reader = csv.reader(f, delimiter=' ')
    #     deck_list = [row for row in reader]
    df = pd.read_csv(deck, delimiter=' ', header=0)
    deck_list = create_deck(df)

    shuffle_deck(deck_list)

    # 無限ループ
    # デッキリストからカードがなくなるまでループする


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--deck', type=str, default='sample_deck.csv')
    args = parser.parse_args()

    deck_play(args)


if __name__ == '__main__':
    main()