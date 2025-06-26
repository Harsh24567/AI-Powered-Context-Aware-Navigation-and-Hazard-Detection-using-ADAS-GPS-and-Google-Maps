from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from env import HazardEnv

env = HazardEnv()

check_env(env, warn=True)

model = PPO("MlpPolicy", env, verbose=1)                  # Initialize PPO Agent

model.learn(total_timesteps=10000)

model.save("hazard_avoidance_agent")
print("Model training completed and saved as 'hazard_avoidance_agent.zip'")
