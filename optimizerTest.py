from GeneticOptimizer import GeneticOptimizer
from random import randint
import numpy as np

def main():
    # testFun = "f(x, y) = 1/(1+(x-3)**2+(y-4)**2) + 1/(.2+(x-6)**2+(y-7)**2)"
    # def func(x, y): return 1/(1+(x-3)**2+(y-4)**2) + 1/(.2+(x-6)**2+(y-7)**2) # Sol. at (3, 4)
    # def func(x, y): return  -(x**2 + y - 11)**2 - (x + y**2 - 7)**2 # Sol. at (3, 2) (-2.805, -3.131) (-3.779, -3.283) (3.584, -1.848)
    # def func(x, y): return -(x + 2*y - 7)**2 - (2*x + y - 5)**2 # Sol. at (1,3)
    # def func(x,y): return -x**2 - y**2 # Sol. at (0, 0)
    # def func(x): return -x**2 # Sol. at (0)
    randFunc = generateRandomFunc()
    f = randFunc["func"]
    o = randFunc["optimum"]
    opt = GeneticOptimizer(f, -10, 10, iter=250, size=100, elitism=0.20, precision=32, tournament_size=30, mutation=0.1)
    (bestDesign, designValues, designFitness, fitnessHistory) = opt.optimize()
    bar = "="*100
    print(f"{bar}\nActual Optimum:\n{o}\n\nDesign String:\n{bestDesign}\n\nDesign Values:\n{designValues}\n\nDesign Fitness:\n{designFitness}\n\nHistory of Fitness:\n{fitnessHistory}\n{bar}\n")


def generateRandomFunc(dims: int = 2, bounds: tuple = (-10, 10), min_vals: int = 3):
    rand_lists = np.random.randint(*bounds, (dims, min_vals))
    coefs = np.random.choice([x+1 for x in range(min_vals)], min_vals, replace=False)
    rand_lists = np.vstack([coefs, rand_lists]).T

    s = "f("
    for i in range(1, dims+1):
        s += f"var_{i}"
        s += ", " if i < dims else ""
    s += ") = "
    for i in range(min_vals):
        s += f"1/({rand_lists[i, 0]}+"
        for j in range(1, dims+1):
            sign = "+" if rand_lists[i, j] >= 0 else ""
            s += f"(var_{j}{sign}{rand_lists[i, j]})**2"
            s += "+" if j < dims else ""
        s += ")"
        s+= " + " if i < min_vals-1 else ""
    
    ind = np.argmin(coefs)
    optimum = list(rand_lists[ind, :])
    opt = [f"var_{i} = {-x}" for i, x in enumerate(optimum)][1:]
    
    return {"func":s, "optimum":opt}


if __name__ == "__main__":
    main()
