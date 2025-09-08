import numpy as np
import matplotlib.pyplot as plt

ph = 0.4
epsilon = 1e-9
epoch = 34


if __name__ == "__main__":
    value = np.zeros(101)
    value[100] = 1
    policy = np.zeros(101)
    delta = 1
    iteration = 0

    # Value iteration
    # while delta >= epsilon:
    #     value_last = value.copy()
    #     for state in np.arange(1, 100):
    #         q_list = []
    #         for action in np.arange(min(state, 100 - state) + 1):
    #             q = ph * value[state + action] + (1 - ph) * value[state - action]
    #             q_list.append(q)
    #         value[state] = max(q_list)
    #     delta = max(abs(value - value_last))
    #     iteration += 1

    for i in range(epoch):
        value_last = value.copy()
        for state in np.arange(1, 100):
            q_list = []
            for action in np.arange(min(state, 100 - state) + 1):
                q = ph * value[state + action] + (1 - ph) * value[state - action]
                q_list.append(q)
            value[state] = max(q_list)
        delta = max(abs(value - value_last))
        iteration += 1

    # Esitmate the policy
    for state in np.arange(1, 100):
        q_list = []
        for action in np.arange(min(state, 100 - state) + 1):
            q = ph * value[state + action] + (1 - ph) * value[state - action]
            q_list.append(q)

        a1 = np.argmax(q_list)
        a2 = np.argmax(np.round(q_list[1:], 5)) + 1
        q1 = q_list[a1]
        q2 = q_list[a2]
        print(f"a1: {a1}")
        print(f"a2: {a2}")
        print(f"q1: {q1}")
        print(f"q2: {q2}")
        policy[state] = np.argmax(np.round(q_list[1:], 5) + 1)  # ignore the zero action

    print(f"iteration times: {iteration}")
    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].plot(value)

    ax[1].scatter(np.arange(1, 100), policy[1:100])

    plt.show()
