import soccer_twos
from typing import Dict
from soccer_twos import AgentInterface
import ray
from ray.rllib.policy.policy import Policy
import pickle
import numpy as np

class RayAgent(AgentInterface):


    def __init__(self):

        ray.init(ignore_reinit_error=True)

        with open("policy_state.pkl", "rb") as f:
            p = pickle.load(f)
        self.policy = Policy.from_state(p)

    def act(self, observation: Dict[int, np.ndarray]) -> Dict[int, np.ndarray]:

        actions = {}
        for player_id in observation:
            actions[player_id], *_ = self.policy.compute_single_action(
                observation[player_id]
            )
        return actions
