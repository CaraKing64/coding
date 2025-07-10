import random, time, pygame


with open("first-names.txt", "r") as doc:
    doclinesold = doc.readlines()
names = []
for line in doclinesold:
    names.append(line.replace("\n", ""))

class Card():
    def __init__(self, special, value, colour) -> None:
        if special not in [False, "wild", "skip"]:
            raise ValueError("Invalid card type initialised")
        if not special:
            if value <= 0 or value > 12:
                raise ValueError("Invalid card number initialised")
            if colour not in ["red", "blue", "green", "yellow"]:
                raise ValueError("Invalid card colour initialised")
            self.value = value
            self.colour = colour
            self.string = self.colour.capitalize() + " " + str(self.value)
        elif special == "wild":
            self.string = "Wild"
        elif special == "skip":
            self.string = "Skip"

    def __str__(self) -> str:
        return(self.string)
    def __repr__(self) -> str:
        return(str(self))

class Player():
    def __init__(self, hand=[], bot=True, name=None):
        self.hand = hand
        self.bot = bot
        if not self.bot and name == None:
            self.name = "Player"
        if self.bot and name == None:
            self.name = random.choice(names)
    def getHand(self) -> str:
        temp = ""
        for i in self.hand:
            temp += f"{i}, "
        return(temp[:-2])
    def __repr__(self) -> str:
        return(self.name)
    def turn(self, game):
        if not self.bot:
            print("Deck with " + str(len(game.deck)) + " cards | Discard pile: " + str(game.discard_pile[0]))
            print("Your hand: " + self.getHand())
        else:
            pass
    def updateCardDict(self):
        self.card_dict = {}
        for card in self.hand:
            self.card_dict[card.string] = card
    def drawCard(draw_pile:list):
        self.hand.append(draw_pile.pop(0))
        self.updateCardDict()
    def discardCard(card_name):
        self.hand.remove(card_name)

class Game():
    def __init__(self, bot_count=1, hand_size=10) -> None:
        self.deck = []
        for colour in range(4):
            colours = ["red", "blue", "green", "yellow"]
            for i in range(1, 13):
                for _ in range(2):
                    new_card = Card(False, i, colours[colour])
                    self.deck.append(new_card)
        for _ in range(8):
            new_card = Card("wild", None, None)
            self.deck.append(new_card)
        for _ in range(2):
            new_card = Card("skip", None, None)
            self.deck.append(new_card)
        random.shuffle(self.deck)

        self.player_count = bot_count + 1
        self.players = []
        self.hand_size = 10
        for i in range(self.player_count):
            is_bot = False if i == 0 else True
            new_hand = self.dealHand(10)
            new_player = Player(new_hand, bot=is_bot, name=None)
            self.players.append(new_player)
        
        self.discard_pile = []
        starting_card = self.deck.pop(0)
        self.discard_pile.insert(0, starting_card)

        self.turn = 0

    def dealHand(self, num=10) -> list:
        hand = []
        for _ in range(num):
            rand_num = random.randint(1, len(self.deck)-1)
            choice = self.deck[rand_num]
            del self.deck[rand_num]
            hand.append(choice)
        return(hand)

def redrawGameWindow():
    screen.fill(colours["tan"])


    card_count = 10
    for c in range(card_count):
        total_card_width = card_count*CARD_WIDTH
        total_gap_width = WIN_WIDTH-total_card_width
        gap_width = total_gap_width/(card_count+1)
        
        gap = 12.8
        left_pos = CARD_WIDTH*(c) + (c+1)*gap_width

        card_visual_rect = pygame.Rect(left_pos, WIN_HEIGHT-CARD_HEIGHT-gap_width, CARD_WIDTH, CARD_HEIGHT)

        pygame.draw.rect(screen, colours["black"], card_visual_rect)
        
    player_count = 3
    other_card_count = 10
    other_win_width = 800
    other_card_height = 100
    other_card_width = 67
    for a in range(player_count):
        player_card_visual_rect = pygame.Rect(20, 20*(a+1)+other_card_height*a, other_card_width, other_card_height)
        pygame.draw.rect(screen, colours["black"], player_card_visual_rect)
        example_text = comic_sans_font.render(f"Player {a}", True, (255, 0, 0))
        screen.blit(example_text, pygame.Rect(30+other_card_width, 20*(a+1)+other_card_height*a+(other_card_height-example_text.get_height())/2-2, other_card_width, other_card_height))


    pygame.display.flip()

WIN_WIDTH = 1280
WIN_HEIGHT = 720
CARD_WIDTH = 100
CARD_HEIGHT = 140


pygame.init()
pygame.font.init()
comic_sans_font = pygame.font.SysFont("Comic Sans MS", 40)

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

colours = {
    "red":(198, 20, 10),
    "green":(58, 107, 42),
    "blue":(46, 68, 154),
    "yellow":(219, 123, 3),
    "tan":(133, 102, 9),
    "black":(0, 0, 0),
    "white":(255, 255, 255),

}


game = Game()
for p in game.players:
    print(p.name, p.hand)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    mouse_pos = pygame.mouse.get_pos()

    #print(mouse_pos)
    
    redrawGameWindow()

    









'''

2 of each card 1-12 for 4 colours
8 wild cards
4 skip cards




Phase 1: 2 sets of 3
Phase 2: 1 set of 3 + 1 run of 4
Phase 3: 1 set of 4 + 1 run of 4
Phase 4: 1 run of 7
Phase 5: 1 run of 8
Phase 6: 1 run of 9
Phase 7: 2 sets of 4
Phase 8: 7 cards of one color
Phase 9: 1 set of 5 + 1 set of 2
Phase 10: 1 set of 5 + 1 set of 3



for c in range(10):
    left_pillar = WIN_WIDTH/2-10
    right_pillar = WIN_WIDTH/2+10
    gap = 20
    offset = CARD_WIDTH+20
    left_positions = [
        (left_pillar+(CARD_WIDTH*-5+20*-4)),
        (left_pillar+(CARD_WIDTH*-4+20*-3)),
        (left_pillar+(CARD_WIDTH*-3+20*-2)),
        (left_pillar+(CARD_WIDTH*-2+20*-1)),
        (left_pillar+(CARD_WIDTH*-1+20*0)),
        (right_pillar+(CARD_WIDTH*0+20*0)),
        (right_pillar+(CARD_WIDTH*1+20*1)),
        (right_pillar+(CARD_WIDTH*2+20*2)),
        (right_pillar+(CARD_WIDTH*3+20*3)),
        (right_pillar+(CARD_WIDTH*4+20*4)),
    ]
    pygame.draw.rect(screen, colours["black"], pygame.Rect(left_positions[c], WIN_HEIGHT-CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))

    #pygame.draw.rect(screen, colours["red"], pygame.Rect(left_pillar, 0, 5, WIN_HEIGHT))
    #pygame.draw.rect(screen, colours["red"], pygame.Rect(right_pillar, 0, 5, WIN_HEIGHT))

main_player_card_rects = [
    pygame.Rect(25.454545454545453, 554.5454545454545, 100, 140)
    pygame.Rect(150.9090909090909, 554.5454545454545, 100, 140)
    pygame.Rect(276.3636363636364, 554.5454545454545, 100, 140)
    pygame.Rect(401.8181818181818, 554.5454545454545, 100, 140)
    pygame.Rect(527.2727272727273, 554.5454545454545, 100, 140)
    pygame.Rect(652.7272727272727, 554.5454545454545, 100, 140)
    pygame.Rect(778.1818181818182, 554.5454545454545, 100, 140)
    pygame.Rect(903.6363636363636, 554.5454545454545, 100, 140)
    pygame.Rect(1029.090909090909, 554.5454545454545, 100, 140)
    pygame.Rect(1154.5454545454545, 554.5454545454545, 100, 140)
]






        
other_card_count = 10
other_win_width = 800
other_card_height = 100
other_card_width = 67
for a in range(player_count):
    for b in range(other_card_count):
        total_card_width = other_card_count*other_card_width
        total_gap_width = other_win_width-total_card_width
        gap_width = total_gap_width/(other_card_count+1)
        
        left_pos = other_card_width*(b) + (b+1)*gap_width

        pygame.draw.rect(screen, colours["black"], pygame.Rect(left_pos, (a)*other_card_height+(a+1)*gap_width, other_card_width, other_card_height))


other_player_card_rects = [
        pygame.Rect(97, 40.0, 67, 100),
        pygame.Rect(97, 160.0, 67, 100),
        pygame.Rect(97, 280.0, 67, 100)
    ]
other_player_text_rects = [
    pygame.Rect(20, 20, 67, 100),
    pygame.Rect(20, 140, 67, 100),
    pygame.Rect(20, 260, 67, 100),
]


'''