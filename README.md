# Teach AI To Play Snake! Reinforcement Learning With PyTorch and Pygame
## 教AI玩贪吃蛇！使用PyTorch和Pygame进行强化学习

### Original repository README:

>In this Python Reinforcement Learning Tutorial series we teach an AI to play Snake! We build everything from scratch using Pygame and PyTorch. The tutorial consists of 4 parts:

>You can find all tutorials on my channel: [Playlist](https://www.youtube.com/playlist?list=PLqnslRFeH2UrDh7vUmJ60YrmWd64mTTKV)

>- Part 1: I'll show you the project and teach you some basics about Reinforcement Learning and Deep Q Learning.
>- Part 2: Learn how to setup the environment and implement the Snake game.
>- Part 3: Implement the agent that controls the game.
>- Part 4: Implement the neural network to predict the moves and train it.

原始仓库：https://github.com/patrickloeber/snake-ai-pytorch

### 针对原始代码添加了一些辅助的新功能：

- AI将会在靠近食物时得到奖励，AI越久没吃到食物，奖励越大(0.005)
- AI将会在远离食物时得到惩罚，AI越久没吃到食物，惩罚越大(0.007)
- 添加了训练过程中reward和iteration的实时显示
- 添加了每局末reward的总和计算并打印
- 修改图表，添加了图例

Original repository: https://github.com/patrickloeber/snake-ai-pytorch

### Added some auxiliary new features for the original code:

- AI will be rewarded when approaching food. The longer AI does not eat food, the greater the reward (0.005)
- AI will be punished when staying away from food. The longer AI does not eat food, the greater the punishment (0.007)
- Added real-time display of reward and iteration during training
- Added sum calculation and print at the end of each round of reward
- Modified chart, added legend
