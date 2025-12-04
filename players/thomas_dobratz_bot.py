"""
Thomas Dobratz Bot - We shall see how it plays
This is the bot I am entering in the tournament
"""
from typing import List, Dict, Any
import random

from bot_api import PokerBotAPI, PlayerAction
from engine.cards import Card, Rank, Suit
from engine.poker_game import GameState

best_preflop_raise = 80 #raise for ACE-ACE
preflop_raise_step = 3 #raise difference between hands
best_preflop_commitment = 0.9 #maximum amount of money willing to bet on ACE-ACE, as percent
preflop_commitment_step = 0.03 #commitment difference between hands

#this is list contianing elements of the form [(card1,card2), is_matching, bet_increment, max_commitment_percent]
preflop_hand_behavior = [
    [(Rank.ACE, Rank.ACE), False,
    best_preflop_raise,
    best_preflop_commitment],
    [(Rank.KING, Rank.KING), False,
    best_preflop_raise - preflop_increment_step,
    best_preflop_commitment - preflop_commitment_step],
    [(Rank.QUEEN, Rank.QUEEN), False,
    best_preflop_raise - (2 * preflop_increment_step),
    best_preflop_commitment - (2 * preflop_commitment_step)],
    [(Rank.JACK, Rank.JACK), False,
    best_preflop_raise - (3 * preflop_increment_step),
    best_preflop_commitment - (3 * preflop_commitment_step)],
    [(Rank.ACE, Rank.KING), True,
    best_preflop_raise - (4 * preflop_increment_step),
    best_preflop_commitment - (4 * preflop_commitment_step)],
    [(Rank.TEN, Rank.TEN), False,
    best_preflop_raise - (5 * preflop_increment_step),
    best_preflop_commitment - (5 * preflop_commitment_step)],
    [(Rank.ACE, Rank.KING), False,
    best_preflop_raise - (6 * preflop_increment_step),
    best_preflop_commitment - (6 * preflop_commitment_step)],
    [(Rank.ACE, Rank.QUEEN), True,
    best_preflop_raise - (7 * preflop_increment_step),
    best_preflop_commitment - (7 * preflop_commitment_step)],
    [(Rank.NINE, Rank.NINE), False,
    best_preflop_raise - (8 * preflop_increment_step),
    best_preflop_commitment - (8 * preflop_commitment_step)],
    [(Rank.ACE, Rank.JACK), True,
    best_preflop_raise - (9 * preflop_increment_step),
    best_preflop_commitment - (9 * preflop_commitment_step)],
    [(Rank.KING, Rank.QUEEN), True,
    best_preflop_raise - (10 * preflop_increment_step),
    best_preflop_commitment - (10 * preflop_commitment_step)],
    [(Rank.ACE, Rank.TEN), True,
    best_preflop_raise - (11 * preflop_increment_step),
    best_preflop_commitment - (11 * preflop_commitment_step)],
    [(Rank.ACE, Rank.QUEEN), False,
    best_preflop_raise - (12 * preflop_increment_step),
    best_preflop_commitment - (12 * preflop_commitment_step)],
    [(Rank.EIGHT, Rank.EIGHT), False,
    best_preflop_raise - (13 * preflop_increment_step),
    best_preflop_commitment - (13 * preflop_commitment_step)],
    [(Rank.KING, Rank.JACK), True,
    best_preflop_raise - (14 * preflop_increment_step),
    best_preflop_commitment - (14 * preflop_commitment_step)],
    [(Rank.KING, Rank.TEN), True,
    best_preflop_raise - (15 * preflop_increment_step),
    best_preflop_commitment - (15 * preflop_commitment_step)],
    [(Rank.QUEEN, Rank.JACK), True,
    best_preflop_raise - (16 * preflop_increment_step),
    best_preflop_commitment - (16 * preflop_commitment_step)],
    [(Rank.ACE, Rank.JACK), False,
    best_preflop_raise - (17 * preflop_increment_step),
    best_preflop_commitment - (17 * preflop_commitment_step)],
    [(Rank.KING, Rank.QUEEN), False,
    best_preflop_raise - (18 * preflop_increment_step),
    best_preflop_commitment - (18 * preflop_commitment_step)],
    [(Rank.QUEEN, Rank.TEN), True,
    best_preflop_raise - (19 * preflop_increment_step),
    best_preflop_commitment - (19 * preflop_commitment_step)]
]

class ThomasDobratzBot(PokerBotAPI):
    """
    This is the poker bot entered by Thomas Dobratz.
    Hopefully it does well.
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.hands_played = 0
    
    def get_action(self, game_state: GameState, hole_cards: List[Card], 
                   legal_actions: List[PlayerAction], min_bet: int, max_bet: int) -> tuple:
        """This handles the decision making."""
        
        # Choose a random legal action
        action = random.choice(legal_actions)
        
        # If raising, choose a random valid amount
        if action == PlayerAction.RAISE:
            # More realistic random raise - between min raise and pot size
            max_raise = min(game_state.pot * 1.5, max_bet) # Raise up to 1.5x pot
            if max_raise < min_bet:
                max_raise = min_bet
                
            amount = random.randint(min_bet, int(max_raise))
            return action, amount
        
        # All other actions don't need an amount
        return action, 0
    
    def hand_complete(self, game_state: GameState, hand_result: Dict[str, Any]):
        """Track hands played"""
        self.hands_played += 1
        
        if self.hands_played > 0 and self.hands_played % 50 == 0:
            self.logger.info(f"Played {self.hands_played} hands randomly")