import numpy as np
from matplotlib import pyplot as plt


def compute_Utility(A_preference, B_preference, A_proportion, source):
    A_utility = []
    B_utility = []
    for offer in A_proportion:
        A_utility.append(round(A_preference[0] * offer[0] + A_preference[1] * offer[1], 2))
        B_utility.append(round(B_preference[0] * (source - offer[0]) + B_preference[1] * (source - offer[1]), 2))
    return A_utility, B_utility


def Pareto_efficient(A_Utility, B_Utility):
    P_list = []
    for i in range(len(A_Utility)):
        for j in range(len(A_Utility)):
            if A_Utility[i] > A_Utility[j] and B_Utility[i] > B_Utility[j]:
                P_list.append(j + 1)
            if A_Utility[i] == A_Utility[j] and B_Utility[i] > B_Utility[j]:
                P_list.append(j + 1)
            if A_Utility[i] > A_Utility[j] and B_Utility[i] == B_Utility[j]:
                P_list.append(j + 1)
    P_list = list(set(range(1, len(A_Utility) + 1)) - set(np.unique(P_list)))
    return P_list


def Utilitarian(A_Utility, B_Utility):
    U_list = []
    for i in range(len(A_Utility)):
        Utility_sum = A_Utility[i] + B_Utility[i]
        U_list.append(Utility_sum)
    return np.argmax(U_list) + 1


def Nash(A_Utility, B_Utility):
    U_list = []
    for i in range(len(A_Utility)):
        Utility_sum = A_Utility[i] * B_Utility[i]
        U_list.append(Utility_sum)
    return np.argmax(U_list) + 1


def Egalitarian(A_Utility, B_Utility):
    min_list = []
    for i in range(len(A_Utility)):
        min_list.append(min(A_Utility[i], B_Utility[i]))

    return np.argmax(min_list) + 1


def Envy_free(A_preference, B_preference, A_proportion, source):
    E_list = []
    A_origin, B_origin = compute_Utility(A_preference, B_preference, A_proportion, source)
    A_proportion = np.array(A_proportion)
    for i in range(len(A_proportion)):
        A_proportion[i] = np.array([source, source]) - A_proportion[i]
    A_change, B_change = compute_Utility(A_preference, B_preference, A_proportion, source)
    print(A_change)
    print(B_change)
    for i in range(len(A_origin)):
        if A_change[i] <= A_origin[i] and B_change[i] <= B_origin[i]:
            E_list.append(i + 1)

    return E_list


if __name__ == '__main__':
    preference_A = [0.25, 0.75]  # in the case U_A = 0.25 * A_1 + 0.75 * A_2
    preference_B = [0.5, 0.5]

    proportion_A = [[1, 1], [1, 0], [0, 1], [0.5, 0.5], [0, 0], [0.8, 0], [0, 0.8]]

    pie = 1
    Utility_A, Utility_B = compute_Utility(preference_A, preference_B, proportion_A, pie)

    print('Utility_A')
    print(Utility_A)
    print('Utility_B')
    print(Utility_B)
    print('Pareto') #####
    print(Pareto_efficient(Utility_A, Utility_B))
    print('Utilitarian : maximise the sum of utilities')
    print(Utilitarian(Utility_A, Utility_B))
    print('Nash : maximise the product of the utility of the agents')
    print(Nash(Utility_A, Utility_B))
    print('Egalitarian : maximise the minimum utility')
    print(Egalitarian(Utility_A, Utility_B))
    print('Envy_free : no agent prefers the resources allocated to other agents')
    print(Envy_free(preference_A, preference_B, proportion_A, pie))
    plt.scatter(Utility_A, Utility_B)
    plt.grid(True)
    n = np.arange(len(proportion_A))
    for i, txt in enumerate(n):
        plt.annotate(txt+1, (Utility_A[i], Utility_B[i]))
    plt.show()

