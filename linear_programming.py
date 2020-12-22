# import the library pulp as p
import pulp as p
from fractions import Fraction
# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMaximize)

# Create problem Variables
x1 = p.LpVariable("x1", lowBound=0) # Create a variable x >= 0
x2 = p.LpVariable("x2", lowBound=0) # Create a variable y >= 0
x3 = p.LpVariable("x3", lowBound=0)
# Objective Function
Lp_prob += 250*x1 + 300*x2 + 400*x3

# Constraints:
Lp_prob += 5*x1 + 3*x2 + 5*x3 <= 100
Lp_prob += 3*x1 + 5*x2 + 3*x3 <= 80

# Display the problem
print(Lp_prob)

status = Lp_prob.solve() # Solver
print(p.LpStatus[status]) # The solution status

# Printing the final solution
print(p.value(x1), p.value(x2), p.value(x3), p.value(Lp_prob.objective))
