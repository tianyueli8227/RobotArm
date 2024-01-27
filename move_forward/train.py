# def main():
#     env = LiftEnv()
#     env.reset()
#     for episode in range(10):
#         for step in range(100):
#             env.render()
#             action = env.action_space.sample()
#             obs, reward, done, info = env.step(action)
#             env.step(action)
#             if done:
#                 print(f'Done at step {step}')
#                 break
#         obs = env.reset()
#     env.close()


# if __name__ == '__main__':
#     main()

import gym
import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import rl_utils
from move_forward import LiftEnv
from PPO import PPO

actor_lr = 1e-3
critic_lr = 1e-2
num_episodes = 500
hidden_dim = 128
gamma = 0.98
lmbda = 0.95
epochs = 10
eps = 0.2
device = torch.device("cuda") if torch.cuda.is_available() else torch.device(
    "cpu")

env = LiftEnv()
env.seed(0)
torch.manual_seed(0)
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n
agent = PPO(state_dim, hidden_dim, action_dim, actor_lr, critic_lr, lmbda,
            epochs, eps, gamma, device)

env.reset()

for episode in range(10):
    for step in range(100):
        env.render()
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        env.step(action)
        if done:
            print(f'Done at step {step}')
            break
    obs = env.reset()
env.close()


# env_name = 'CartPole-v0'
# env = gym.make(env_name)
# env.seed(0)
# torch.manual_seed(0)
# state_dim = env.observation_space.shape[0]
# action_dim = env.action_space.n
# agent = PPO(state_dim, hidden_dim, action_dim, actor_lr, critic_lr, lmbda,
#             epochs, eps, gamma, device)

# return_list = rl_utils.train_on_policy_agent(env, agent, num_episodes)