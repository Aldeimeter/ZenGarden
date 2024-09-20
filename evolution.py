import random
import copy

invalid_positions = ((0,0),(11,9),(0,9),(11,0))


turn_table = {
    "left": {
        "right": "down",
        "left": "up",
        "down": "left",
        "up": "right"
    },
    "right": {
        "right":"up",
        "left": "down",
        "down": "right",
        "up": "left"
    }
}



def print_field(field):
    col_width = 2
    for row in field:
        print(" ".join(f"{num:{col_width}}" for num in row))
    print("\n")


def generate_field(field_props):
    columns, rows, stones = field_props
    field = [[0] * columns for i in range(rows)]
    for stone in stones:
        x, y = stone 
        field[y][x] = -1
    return field


def generate_start_positions(field_props, positions):
    length, width, _ = field_props
    pos_1 =  (random.randint(0, 1) * (length -1), random.randint(0, width - 1))
    pos_2 =  (random.randint(0, length - 1), random.randint(0, 1) * (width -1))
    if pos_1 == pos_2:
        return 
    if pos_1 in positions or pos_2 in positions:
        return 
    if pos_1 == invalid_positions or pos_2 == invalid_positions:
        return 

    return pos_1, pos_2


def generate_genes(field_props):
    positions = []
    turns = []
    length, width, stones = field_props

    while len(positions) < length + width:
        result = generate_start_positions(field_props, positions)
        if not result:
            continue
        pos_1, pos_2 = result
        positions.append(pos_1);
        positions.append(pos_2);
    while len(turns) < len(stones):
        turns.append("right" if random.randint(0, 1) == 0 else "left");

    return { "positions": positions, "turns": turns, "fitness": 0} 


def initialization(field_props, population_size):
    return [generate_genes(field_props) for i in range(population_size)]


def check_direction(position):
    if position[0] == 0:
        return "right"
    if position[0] == 11:
        return "left"
    if position[1] == 0:
        return "down"
    if position[1] == 9:
        return "up"


def fitness(individual, field_props):
    positions, turns, fitness = individual.values()
    step = 1
    turn = 0
    field = generate_field(field_props)
    for position in positions:
        if field[position[1]][position[0]] != 0:
            continue
        else:
            field[position[1]][position[0]] = step
            individual["fitness"] += 1
        direction = check_direction(position)
        turn_count = 0
        while True:
            # print(position)
            # if edge reached -> go to next starting position 
            if position[0] == 0 and direction == "left":
                step += 1
                break
            if position[0] == 11 and direction == "right":
                step += 1
                break
            if position[1] == 1 and direction == "up":
                step += 1
                break
            if position[1] == 9 and direction == "down":
                step += 1
                break

            if direction == "right" and position[0] + 1 < len(field[0]) and field[position[1]][position[0] + 1] == 0:
                position = (position[0] + 1, position[1])
                field[position[1]][position[0]] = step
                individual["fitness"] += 1
            elif direction == "left" and position[0] - 1 >= 0 and field[position[1]][position[0] - 1] == 0:
                position = (position[0] - 1, position[1])
                field[position[1]][position[0]] = step
                individual["fitness"] += 1
            elif direction == "down" and position[1] + 1 < len(field) and field[position[1] + 1][position[0]] == 0:
                position = (position[0], position[1] + 1)
                field[position[1]][position[0]] = step
                individual["fitness"] += 1
            elif direction == "up" and position[1] - 1 >= 0 and field[position[1] - 1][position[0]] == 0:
                position = (position[0], position[1] - 1)
                field[position[1]][position[0]] = step
                individual["fitness"] += 1
            # if move is impossible -> turn 
            # Edge case:
            #   no further move possible -> finish
            else:

                if not (turn < len(turns)):
                    turn = 0
                direction = turn_table[turns[turn]][direction]
                turn_count +=1
                turn += 1
                if turn_count == 4:    
                    step += 1
                    break

    return individual


def evaluation(population, field_props):
    new_population = copy.deepcopy(population)
    return [fitness(individual, field_props) for individual in new_population] 


def tournament(population, desired_amount):
    new_population = []
    while len(new_population) < desired_amount:
        selected = random.sample(population, 3)
        new_population.append(max(selected, key=lambda individual: individual["fitness"]))
    return new_population


def roulette(population, desired_amount):
    new_population = random.choices(population, weights=[individual["fitness"] for individual in population], k=desired_amount)
    return new_population 


def rank_based(population, desired_amount):
    new_population = sorted(population, key=lambda individual: individual["fitness"], reverse=True)[:desired_amount]
    return new_population


def selection(population, selection_function, desired_amount):
    return selection_function(population, desired_amount)
    

def single_point_crossover(parent_1, parent_2):
    position_point = random.randint(0, len(parent_1["positions"]) - 1)
    turns_point = random.randint(0, len(parent_1["turns"]) - 1)
    offspring_1 = {
        "positions": parent_1["positions"][:position_point] + parent_2["positions"][position_point:],
        "turns": parent_1["turns"][:turns_point] + parent_2["turns"][turns_point:],
        "fitness": 0
    }
    offspring_2 = {
        "positions": parent_2["positions"][:position_point] + parent_1["positions"][position_point:],
        "turns": parent_2["turns"][:turns_point] + parent_1["turns"][turns_point:],
        "fitness": 0 
    }
    return offspring_1, offspring_2


def uniform_crossover(parent_1, parent_2):
    position_mask = [random.randint(0, 1) for i in range(len(parent_1["positions"]))]
    turn_mask = [random.randint(0, 1) for i in range(len(parent_1["turns"]))]

    positions_1 = []
    positions_2 = []

    turns_1 = []
    turns_2 = []
    
    for i, bit in enumerate(position_mask): 
        if bit == 0:
            positions_1.append(parent_1["positions"][i])
            positions_2.append(parent_2["positions"][i])
        else:
            positions_1.append(parent_2["positions"][i])
            positions_2.append(parent_1["positions"][i])
    for i, bit in enumerate(turn_mask): 
        if bit == 0:
            turns_1.append(parent_1["turns"][i])
            turns_2.append(parent_2["turns"][i])
        else:
            turns_1.append(parent_2["turns"][i])
            turns_2.append(parent_1["turns"][i])

    offspring_1 = {
        "positions": positions_1,
        "turns": turns_1,
        "fitness": 0,
    }
    offspring_2 = {
        "positions": positions_2,
        "turns": turns_2,
        "fitness": 0,
    }

    return offspring_1, offspring_2


def crossover(population, crossover_function):
    return [child for i in range(0, len(population) - 1, 2) for child in crossover_function(population[i], population[i+1])]


def mutate(individual, mutation_rate, field_props):
    for i in range(len(individual["positions"])):
        if random.random() < mutation_rate:
            result = None
            while not result:
                result = generate_start_positions(field_props, individual["positions"])
            pos_1, pos_2 = result
            individual["positions"][i] = pos_1 if random.randint(0, 1) == 0 else pos_2  
    for i in range(len(individual["turns"])):
        if random.random() < mutation_rate:
            individual["turns"][i] = "right" if random.randint(0, 1) == 0 else "left"
    return individual


def mutation(population, mutation_rate, field_props):
    new_population = copy.deepcopy(population)
    return [mutate(indiviual, mutation_rate, field_props) for indiviual in new_population]

def elitism(population, elitism_rate):
    sorted_population = sorted(population, key=lambda individual: individual["fitness"], reverse=True)
    return sorted_population[:int(len(population) * elitism_rate)]


def main(preferences=None):
    if preferences is None:
        population_size = 100
        mutation_rate = 0.10
        elitism_rate = 0.05
        field_props =(12, 10, [(1,2),(2,4),(4,3),(5,1),(8,6),(9,6)])
        amount_of_generations = 100
        selection_function = roulette
        crossover_function = single_point_crossover
        offspring_factor = 3/4
    else:
        population_size = preferences["population_size"]
        mutation_rate = preferences["mutation_rate"]
        elitism_rate = preferences["elitism_rate"]
        field_props = preferences["field_props"]
        amount_of_generations = preferences["amount_of_generations"]
        selection_function = roulette if preferences["selection_function"] == "roulette" else tournament
        crossover_function = single_point_crossover if preferences["crossover_function"] == "single_point_crossover" else uniform_crossover
        offspring_factor = preferences["offspring_factor"] 

    fitnesses = []
    populations = []   
    population = initialization(field_props,100) 

    while True:
        populations.append(evaluation(population, field_props))
    
        fitnesses.append(max(populations[-1], key=lambda individual: individual["fitness"])["fitness"])

        # print(f"Best fitness in generation {len(populations)}: {fitnesses[-1]}")

        if len(populations) == amount_of_generations:
            break
        if fitnesses[-1] == field_props[0] * field_props[1] - len(field_props[2]):
            break

        future_population = copy.deepcopy(populations[-1])

        new_population = elitism(population, elitism_rate)

        future_population = selection(future_population, selection_function, int((population_size * offspring_factor))) 
        
        future_population = crossover(future_population, crossover_function)
        
        new_population += mutation(future_population, mutation_rate, field_props)
        
        new_population += initialization(field_props, population_size - len(new_population))
        
        population = new_population
    
    print(f"Best fitness over {len(populations)} generations: {max(fitnesses)}")
    with open("results", "a") as myfile:
        myfile.write(str(max(fitnesses)) + "\n")


if __name__ == "__main__":
    main()


