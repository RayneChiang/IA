

from fractions import Fraction


def calculate_expect(prob_1, prob_2, Utilties):
    return prob_1 * prob_2 * Utilties[0] + prob_1 * (1 - prob_2) * Utilties[1] + (1 - prob_1) * prob_2 * Utilties[2] + (
            1 - prob_1) * (1 - prob_2) * Utilties[3]


def indifference(prob, Utilities):
    EU_left = prob * Utilities[0] + (1 - prob) * Utilities[1]
    EU_right = prob * Utilities[2] + (1 - prob) * Utilities[3]

    return [EU_left, EU_right]

def solve(eq, var='x'):
    eq = eq.replace("=", "-(")+")"
    c = eval(eq, {var:1j})
    return Fraction(-Fraction(c.real)/Fraction(c.imag))


def computer_mixed_Nash(Utilities):
    eq1 = str(Utilities[0])+'*x+'+str(Utilities[1])+'*(1-x)'
    eq2 = str(Utilities[2])+'*x+'+str(Utilities[3])+'*(1-x)'
    equation = eq1+"="+eq2
    mix_Nash = solve(equation, var='x')
    return mix_Nash

if __name__ == '__main__':

    # # fill in here
    # prob_1 = Fraction(1, 3)
    # prob_2 = Fraction(3, 4)
    # Utilities_1 = [3, 0, 2, 1]  # first top then bottom
    # Utilities_2 = [1, 3, 4, 1]  # first left then right

    prob_1 = Fraction(1, 2)
    prob_2 = Fraction(1, 2)
    Utilities_1 = [6, -1, 11, -3]
    Utilities_2 = [6, -1, 11, -3]

    result_1 = Fraction(calculate_expect(prob_1, prob_2, Utilities_1))
    result_2 = Fraction(calculate_expect(prob_2, prob_1, Utilities_2))
    print("Utility of player one: " + str(result_1))
    print("Utility of player two: " + str(result_2))

    print("indifference of player one" + str(indifference(prob_2, Utilities_1)))

    print("indifference of player two" + str(indifference(prob_1, Utilities_2)))
    # Indifference

    print("Mixed nash" + '['+str(computer_mixed_Nash(Utilities_2))+ " "+ str(computer_mixed_Nash(Utilities_1))+"]")


