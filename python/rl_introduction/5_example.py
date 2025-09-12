import numpy as np
import random
from collections import defaultdict

# 状态：s1:手牌总和（12-21） s2:庄家显示的牌（A-10） s3:A是否可用 s4:庄家手牌总和
# 动作：要牌，停牌
# 策略输入：状态 输出：动作

gamma = 1
epochs = 1000

s1 = np.arange(12, 21 + 1)
s2 = np.arange(1, 10 + 1)
s3 = np.arange(2)  # 0:不可用 1:可用
actions = np.arange(2)  # 0:停牌 1:要牌

policy = defaultdict(lambda: 0)  # pi(s)
q = defaultdict(lambda: 0)  # q(s,a)
states_record = np.zeros(10, 10, 2)  # 记录状态是否出现过
state_list = []

rng = np.random.default_rng()


def UpdateStates(states, first_init=False, house_states=None):
    new_card = rng.choice(np.arange(1, 14))
    new_s2 = states[2]
    # Update card point
    if new_card == 11:
        if states[2] == 1:
            new_card_point = 1
        else:
            new_card_point = 11
            new_s2 = 1
    elif new_card > 1 and new_card < 10:
        new_card_point = new_card
    else:
        new_card_point = 10
    # Update s0
    new_s0 = states[0] + new_card_point
    if new_s0 > 21 and states[2] == 1:
        new_s0 -= 10
        new_s2 == 0
    # Update s1
    if first_init:
        new_s1 = 1 if house_states[0] == 11 else house_states[0]
    else:
        new_s1 = states[1]

    state_list.append((new_s0, new_s1, new_s2))

    return new_s0, new_s1, new_s2


def Return(states, house_states):
    # 玩家回合
    action = policy[states]
    while action == 1:  # hit
        states = UpdateStates(states)
        if states[0] > 21:
            return -1
        if states[0] == 21:
            break
        action = policy[states]

    # 庄家回合
    while house_states[0] < 17:
        house_states = UpdateStates(house_states)

    # 庄家爆牌
    if house_states[0] > 21:
        return 1

    # 点数比较
    if states[0] > house_states[0]:
        return 1
    elif states[0] < house_states[0]:
        return -1
    else:
        return 0  # 平局


def MonteCarloExploringStarts():
    # 初始化

    for epoch in range(epochs):
        # 初始化每一幕
        states = (0, 0, 0)
        house_states = (0, 0, 0)
        house_states = UpdateStates(house_states)
        states = UpdateStates(states, True, house_states)
        house_states = UpdateStates(house_states)
        states = UpdateStates(states)

        G = Return(states, house_states)
        # 策略估计
        # q[(state1,state2,state3,action)] = q[(state1,state2,state3,action)] + 1 / (epoch + 1) * (
        #     Return(state1, state2, state3) - q[(state1,state2,state3,action)]
        # )

        # 策略更新
        # idx = np.argmax(Q)
        # i, j, k = np.unravel_index(idx, Q.shape)
        # policy[i][j][k] =
    pass


if __name__ == "__main__":
    pass
