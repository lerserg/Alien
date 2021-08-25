import io
import os.path
import json


class GameStats:
    """Tracking game statistics"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.load_high_score() or 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Saves high score to file"""
        high_score = {'high_score': self.high_score}
        with open(self.settings.save_file, 'w') as f:
            json.dump(high_score, f)

    def load_high_score(self):
        """Loads high score from file"""
        if os.path.exists(self.settings.save_file):
            with open(self.settings.save_file, 'r') as f:
                if f.read().strip():
                    f.seek(io.SEEK_SET)
                return int(json.load(f)['high_score'])
