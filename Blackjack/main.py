from unicodedata import name
import pygame, random, sys, os
pygame.init()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

colours = {
    "light_green":(51, 255, 51)
}

class Card:
    def __init__(self, name:str) -> None:
        self.fname = f"{ROOT_DIR}/img/resize/{name}"
        self.name = name.replace(".png","")
        names_split = self.name.split("_")
        self.suit = names_split[0]
        self.value = names_split[1]
        self.img = pygame.image.load(self.fname)
        self.pos=()
    def __str__(self) -> str:
        return self.name
    def render(self, game, pos=None):
        if pos == None:
            pos = self.pos
        game.screen.blit(self.img, pos)

        
class Deck():
    def __init__(self, deck_count:int=1, shuffled:bool=True) -> None:
        self.deck_count = deck_count        
        self.cards = []
        self.card_names = []
        for _ in range(self.deck_count):
            names = ['clubs_10.png', 'clubs_2.png', 'clubs_3.png', 'clubs_4.png', 'clubs_5.png', 'clubs_6.png', 'clubs_7.png', 'clubs_8.png', 'clubs_9.png', 'clubs_k.png', 'clubs_k.png', 'clubs_k.png', 'clubs_k.png', 'diamonds_10.png', 'diamonds_2.png', 'diamonds_3.png', 'diamonds_4.png', 'diamonds_5.png', 'diamonds_6.png', 'diamonds_7.png', 'diamonds_8.png', 'diamonds_9.png', 'diamonds_k.png', 'diamonds_k.png', 'diamonds_k.png', 'diamonds_k.png', 'hearts_10.png', 'hearts_2.png', 'hearts_3.png', 'hearts_4.png', 'hearts_5.png', 'hearts_6.png', 'hearts_7.png', 'hearts_8.png', 'hearts_9.png', 'hearts_k.png', 'hearts_k.png', 'hearts_k.png', 'hearts_k.png', 'spades_10.png', 'spades_2.png', 'spades_3.png', 'spades_4.png', 'spades_5.png', 'spades_6.png', 'spades_7.png', 'spades_8.png', 'spades_9.png', 'spades_k.png', 'spades_k.png', 'spades_k.png', 'spades_k.png']
            if shuffled:
                random.shuffle(names)
            for deck_card in names:
                card = Card(deck_card)
                self.cards.append(card)
                self.card_names.append(str(card))
    def __str__(self) -> str:
        return str(self.card_names)
    def __getitem__(self, item) -> Card:
        return self.cards[item]
    def __len__(self) -> int:
        return len(self.cards)

class Game():
    def __init__(self, deck_count:int=6):
        self.run = True
        self.window_width, self.window_height, = 1200, 800
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.shoe = Deck(deck_count)
        self.cards_in_play = []
    def new_round(self):
        self.cards_in_play = []
        self.cards_in_play.append(random.choice(self.shoe.cards))
    def tick(self):
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.new_round()




        self.screen.fill(colours["light_green"])
        
        for card in self.cards_in_play:
            card.render(self, (500,300))
        pygame.display.flip()

def main():
    game = Game()
    deck = game.shoe
    for c in deck:
        print(c, c.suit, c.value)

    game.new_round()
    while game.run: #GAMELOOP
        game.tick()

if __name__ == '__main__':
    try:
        main()
        print("Program finished without issues")
        pygame.quit()
        sys.exit(0)
    except KeyboardInterrupt:
        print ("Program stopped by user.")
        pygame.quit()
        sys.exit(1)