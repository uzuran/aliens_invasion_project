class Stats:

    def __init__(self):
        """initilization"""
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        self.ship_life = 3


