import gym
from gym import spaces
import numpy as np
import random

class HazardEnv(gym.Env):
    """
    Custom Environment for hazard-aware autonomous navigation.
    Agent must respond to detected hazards using discrete actions.
    """
    def __init__(self):
        super(HazardEnv, self).__init__()

        self.hazard_types = ['clear', 'red_light', 'roadblock', 'accident']         # Hazard types: 0 = no hazard, 1 = red light, 2 = roadblock, 3 = accident
        self.current_hazard = 0

        self.action_space = spaces.Discrete(4)                                          # Action space: 0 = STOP, 1 = SLOW, 2 = GO, 3 = REROUTE

        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)            # Observation: one-hot vector of current hazard

    def reset(self):
        self.current_hazard = random.randint(0, 3)
        return self._get_obs()

    def _get_obs(self):
        obs = np.zeros(4)
        obs[self.current_hazard] = 1
        return obs

    def step(self, action):
        reward = 0
        done = False

        # Decision rules
        if self.current_hazard == 0 and action == 2:  # GO on clear
            reward = 1
        elif self.current_hazard == 1 and action == 0:  # STOP at red light
            reward = 1
        elif self.current_hazard == 2 and action == 3:  # REROUTE at block
            reward = 1
        elif self.current_hazard == 3 and action in [0, 3]:  # STOP or REROUTE at accident
            reward = 1
        else:
            reward = -1  # Wrong action

        self.current_hazard = random.randint(0, 3)                  # Sample new hazard for next step
        obs = self._get_obs()

        return obs, reward, done, {}

    def render(self, mode='human'):
        print(f"Current hazard: {self.hazard_types[self.current_hazard]}")
