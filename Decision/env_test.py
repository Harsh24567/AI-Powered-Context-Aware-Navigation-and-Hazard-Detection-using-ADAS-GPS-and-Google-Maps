from env import HazardEnv

env = HazardEnv()
obs = env.reset()

for _ in range(5):
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
    env.render()
    print(f"Action: {action}, Reward: {reward}\n")
