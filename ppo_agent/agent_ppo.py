import soccer_twos
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from typing import Dict
from soccer_twos import AgentInterface
import ray
from ray.rllib.policy.policy import Policy
import pickle
import numpy as np
import gym

class RayAgent(AgentInterface):


    def __init__(self, env: gym.Env):

        ray.init(ignore_reinit_error=True)
        weights_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "policy_state.pkl"
        )
        with open(weights_path, "rb") as f:
            p = pickle.load(f)
        self.policy = Policy.from_state(p)

    def act(self, observation: Dict[int, np.ndarray]) -> Dict[int, np.ndarray]:

        actions = {}
        for player_id in observation:
            actions[player_id], *_ = self.policy.compute_single_action(
                observation[player_id]
            )
        return actions