# list of all preferences tried can be found in file: stats 
# possible selection functions: roulette, tournament, rank_based
# possible crossover functions: single_point_crossover, uniform_crossover




# 95.1 % solutions in 1000 test runs
preferences_1 = {
    "amount_of_generations": 100,
    "crossover_function": "single_point_crossover",
    "elitism_rate": 0,
    "field_props": (12, 10, [(1, 2), (2, 4), (4, 3), (5, 1), (8, 6), (9, 6)]),
    "mutation_rate": 0.01,
    "population_size": 100,
    "selection_function": "tournament",
    "offspring_factor": 3/4,
} 
