import matplotlib.pyplot as plt
from IPython import display

def plot(scores, mean_scores, reward):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()

    # # 设置图表窗口尺寸，宽度为12，高度为8
    # plt.figure(figsize=(10, 8))

    # 上面的图表，显示scores和mean_scores
    # plt.subplot(2, 1, 1)  # 2行1列的布局，当前是第1个子图
    plt.title('Training - Scores')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores, label='scores')
    plt.plot(mean_scores, label='mean scores')
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.legend()

    # 下面的图表，单独显示reward
    # plt.subplot(2, 1, 2)  # 当前是第2个子图
    # plt.title('Training - Reward')
    # plt.xlabel('Number of Games')
    # plt.ylabel('Reward')
    # plt.plot(reward, label='reward', color='orange')
    # plt.ylim(min(reward) - 1, max(reward) + 1)
    # plt.text(len(reward)-1, reward[-1], str(reward[-1]))
    # plt.legend()

    plt.tight_layout()  # 调整子图布局
    plt.show(block=False)
    plt.pause(.1)
