from evolution import main
import os
import pprint
import time 

if __name__ == "__main__":

    if os.path.exists("./results"):
        os.remove("./results")
    # possible selection functions: roulette, tournament, rank_based
    # possible crossover functions: single_point_crossover, uniform_crossover
    preferences = {
        "population_size": 100,
        "mutation_rate": 0.01,
        "elitism_rate" : 0,
        "field_props": (12, 10, [(1,2),(2,4),(4,3),(5,1),(8,6),(9,6)]),
        "amount_of_generations": 100,
        "selection_function": "tournament",
        "crossover_function": "single_point_crossover"
    }

    test_runs = 100

    start_time = time.time()
    for i in range(test_runs):
        print(f"Test run {i+1}")
        main(preferences)

    end_time = time.time()
    print("Finished in " + time.ctime(end_time - start_time))
    with open("results", "r") as f:
        results = f.read()

    
    solution_fitness = preferences["field_props"][0] * preferences["field_props"][1] - len(preferences["field_props"][2])
    solutions = results.split('\n').count(str(solution_fitness))
    print(f"Found {solutions} solutions in {test_runs} test runs")
    solution_percentage = solutions / test_runs * 100
    with open("stats", "a") as stats:
        stats.write("------------BEGIN------------\n")
        stats.write(f"Preferences:\n {pprint.pformat(preferences).replace('{','').replace('}','').replace('\'','')}\n")
        stats.write(f"Found {solutions} solutions in {test_runs} test runs\n")
        stats.write(f"{solution_percentage} % in {preferences['amount_of_generations']} generations and {preferences['population_size']} population_size\n")
        stats.write("------------END------------\n")
