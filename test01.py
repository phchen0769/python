import random

# 参数设定
POP_SIZE = 50  # 种群大小
NUM_GENERATIONS = 10  # 迭代代数
MUTATION_RATE = 0.1  # 变异概率
CROSSOVER_RATE = 0.7  # 交叉概率


# 根据所选数字选项设定 x 和 y 的范围
expressions = [
    {"expression": "x**2 + 2*y", "x": [0, 6], "y": [-2, 2]},
    {"expression": "2*x**2 - y**2", "x": [-1, 5], "y": [-3, 1]},
    {"expression": "abs(x) + y", "x": [-2, 4], "y": [-4, 0]},
    {"expression": "-x**2 + 2*y**2", "x": [-3, 3], "y": [0, 4]},
    {"expression": "x**2 - abs(y)", "x": [-4, 2], "y": [1, 5]},
    {"expression": "4*x - 2*y", "x": [-5, 1], "y": [-1, 3]},
    {"expression": "3*abs(x) + y**2", "x": [-6, 0], "y": [-2, 2]},
    {"expression": "2*x**2 - 3*abs(y)", "x": [0, 6], "y": [-3, 1]},
    {"expression": "-x**2 + 3*y**2", "x": [-1, 5], "y": [-4, 0]},
    {"expression": "x + y", "x": [-2, 4], "y": [0, 4]},
    {"expression": "abs(x) - 2*y", "x": [-3, 3], "y": [1, 5]},
    {"expression": "x**2 - 2*y", "x": [-4, 2], "y": [-1, 3]},
    {"expression": "x**2 + 2*abs(y)", "x": [-5, 1], "y": [-2, 2]},
    {"expression": "-x**2 - y**2", "x": [-6, 0], "y": [-3, 1]},
    {"expression": "3*abs(x) - y**2", "x": [0, 6], "y": [-4, 0]},
    {"expression": "2*x + y", "x": [-1, 5], "y": [0, 4]},
    {"expression": "x + 2*y", "x": [-2, 4], "y": [1, 5]},
    {"expression": "4*abs(x) + 2*y", "x": [-3, 3], "y": [-1, 3]},
    {"expression": "abs(x) + y", "x": [-4, 2], "y": [-2, 2]},
    {"expression": "-2*abs(x) + y", "x": [-5, 1], "y": [-3, 1]},
    {"expression": "abs(x) - y**2", "x": [-6, 0], "y": [-4, 0]},
    {"expression": "x**2 - y**2", "x": [0, 6], "y": [0, 4]},
    {"expression": "2*abs(x) + 3*y", "x": [-1, 5], "y": [1, 5]},
    {"expression": "x*y + y", "x": [-2, 4], "y": [-1, 3]},
    {"expression": "x + x*y", "x": [-3, 3], "y": [-4, 0]},
]


# 更新目标函数以接收表达式字符串
def target_function(x, y, expression_str):
    return eval(expression_str)


# 更新适应度函数以接收表达式字符串
def fitness(individual, expression_str):
    x, y = individual
    return target_function(x, y, expression_str)


# 初始化种群函数
def init_population(pop_size, x_range, y_range):
    return [
        (random.uniform(*x_range), random.uniform(*y_range)) for _ in range(pop_size)
    ]


# 变异函数
def mutate(individual, x_range, y_range):
    x, y = individual
    if random.random() < MUTATION_RATE:
        x += random.uniform(-1, 1) * (x_range[1] - x_range[0]) * MUTATION_RATE
        y += random.uniform(-1, 1) * (y_range[1] - y_range[0]) * MUTATION_RATE
    # 确保变异后的值仍然在允许的范围内
    x = max(min(x, x_range[1]), x_range[0])
    y = max(min(y, y_range[1]), y_range[0])
    return (x, y)


# 选择函数
def select(population):
    weights = [fitness(individual, expression_str) for individual in population]
    if sum(weights) <= 0:
        raise ValueError("Total of weights must be greater than zero")
    return random.choices(population, weights=weights, k=2)


# 交叉函数
def crossover(parent1, parent2):
    x1, y1 = parent1
    x2, y2 = parent2
    if random.random() < CROSSOVER_RATE:
        return (x1, y2), (x2, y1)
    else:
        return parent1, parent2


if __name__ == "__main__":
    for expr_dct in expressions:
        # 设定x与y的取值范围
        x_range = expr_dct["x"]
        y_range = expr_dct["y"]
        # 获取表达式字符串
        expression_str = expr_dct["expression"]

        # 创建初始种群
        population = init_population(POP_SIZE, x_range, y_range)

        # 代数迭代
        for generation in range(NUM_GENERATIONS):
            new_population = []
            while len(new_population) < POP_SIZE:
                # 选择
                parent1, parent2 = select(population)
                # 交叉
                child1, child2 = crossover(parent1, parent2)
                # 变异
                child1 = mutate(child1, x_range, y_range)
                child2 = mutate(child2, x_range, y_range)
                # 加入新种群
                new_population.extend([child1, child2])

            population = new_population[:POP_SIZE]

            # 打印当前代的最佳适应度
            print(
                f"Generation {generation} best fitness: {max(fitness(individual, expression_str) for individual in population)}"
            )

        # 找到并打印最终的最佳解
        best_individual = max(population, key=lambda ind: fitness(ind, expression_str))
        print(
            f"Function:{expression_str},best individual: {best_individual} with fitness: {fitness(best_individual, expression_str)}"
        )
