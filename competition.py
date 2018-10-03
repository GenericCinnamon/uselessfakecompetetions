import yaml
import random
import logging

def load_config(filename="config.yml"):
    try:
        with open(filename, 'r') as f:
            return yaml.load(f)
    except FileNotFoundError as e:
        logging.error(f"Could not load config file {filename} with error {e}")

def run_comp(players):
    results = {}
    for player_name in players:
        logging.debug(f"processing player {player_name}")
        player = players[player_name]
        result = random.randint(0, player['max'])
        results[player_name] = result
        logging.debug(f"player {player_name} scored {result}")
    return results

def pretty_print_results(measure, results):
    results_list = sorted([{'name': person_name, 'result': results[person_name]} for person_name in results], key=lambda x : x['result'], reverse=True)
    
    output = ""
    output += f"The results of the {measure} competetion are...\n"
    for i, result in enumerate(results_list):
        output += f"{result['name']} is in position {i+1} with {result['result']}\n"
    return output 

if __name__ == "__main__":
    # Load config
    config = load_config()

    if config is not None:
        try:
            logging.info(f"Loaded config {config}")
            players = config["players"]
            measure = config["measure"]

            # Run the comp if we have any players
            if len(players):
                results = run_comp(players)
                logging.info(results)
                print(pretty_print_results(measure, results))
            else:
                print("No players specified")
        except KeyError as e:
            logging.error(f"Couldn't find config items with error {e}")

