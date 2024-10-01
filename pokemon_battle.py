import requests
import sys
import os

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.data = self.get_data()
        self.stats = self.get_stats()
        self.type = self.get_types()

    def __str__(self):
        print_info = f"This pokemon's name is {self.name}.\nType: \n"
        return print_info

    def get_data(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            sys.exit("Error, pokemon not found")

    def get_stats(self):
        if self.data:
            pokemon_data = self.data
            pokemon_info = {
                "name": pokemon_data["name"],
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "id": pokemon_data["id"]
            }
    # NEED TO FIX THIS MESS
    def get_types(self):
            pokemon_data = self.data
            types = pokemon_data.get("types", [])
            types_len = len(types)

            # Assigns the pokemon type, if there are 2 types they are concatenated.
            if types_len == 1:
                return f"{types[0]['type']['name']}
            if types_len == 2:
                return f"{types[0]['type']} + / + {types[1]['type']['name']}"

def main():
    pokemon1 = Pokemon("pikachu")
    print(pokemon1)
    pokemon2 = Pokemon("pidgey")
    print(pokemon2)

if __name__ == "__main__":
    main()