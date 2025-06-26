from stable_baselines3 import PPO
from env import HazardEnv
import time

model = PPO.load("hazard_avoidance_agent")

env = HazardEnv()
obs = env.reset()

print("🔁 Running agent evaluation...\n")

for step in range(20):               # 20 decision steps
    env.render()
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    
    print(f"Step {step + 1}")
    print(f"Action Taken: {['STOP', 'SLOW', 'GO', 'REROUTE'][action]}")
    print(f"Reward: {reward}")
    print("–––––––––––––––––––––––––––––")
    
    time.sleep(1) 

print("✅ Evaluation complete.")
