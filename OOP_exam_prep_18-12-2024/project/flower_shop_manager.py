from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    VALID_PLANTS = {"Flower": Flower, "LeafPlant": LeafPlant}
    VALID_CLIENTS = {"RegularClient": RegularClient, "BusinessClient": BusinessClient}

    def __init__(self):
        self.income = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(
        self,
        plant_type: str,
        plant_name: str,
        plant_price: float,
        plant_water_needed: int,
        plant_extra_data: str,
    ):
        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")
        plant = self.VALID_PLANTS[plant_type](
            plant_name, plant_price, plant_water_needed, plant_extra_data
        )
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")

        try:
            self.filter_clients_by_phone(client_phone_number)[0]
            raise ValueError("This phone number has been used!")
        except IndexError:
            client = self.VALID_CLIENTS[client_type](client_name, client_phone_number)
            self.clients.append(client)
            return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(
        self, client_phone_number: str, plant_name: str, plant_quantity: int
    ):
        client = self.filter_clients_by_phone(client_phone_number)
        try:
            client = client[0]
        except IndexError:
            raise ValueError("Client not found!")

        plants = [plant for plant in self.plants if plant.name == plant_name]
        if not plants:
            raise ValueError("Plants not found!")

        if plant_quantity > len(plants):
            return "Not enough plant quantity."

        plants = plants[:plant_quantity]
        total_sum = sum([p.price for p in plants]) # 62
        total_sum = total_sum - client.discount * total_sum /100

        self.income += total_sum
        # helper_count = 0
        for p in plants:
            self.plants.remove(p)
            # helper_count += 1
            # if helper_count == plant_quantity:
            #     break

        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {total_sum:.2f}"

    def remove_plant(self, plant_name: str):
        plants = [plant for plant in self.plants if plant.name == plant_name]
        if not plants:
            return "No such plant name."
        plant = plants[0]
        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        clients_no_orders = [c for c in self.clients if c.total_orders == 0]
        count = len(clients_no_orders)
        for c in clients_no_orders:
            self.clients.remove(c)
        return f"{count} client/s removed."

    def shop_report(self):
        unsold_flowers = {}
        for plant in self.plants:
            if plant.name not in unsold_flowers:
                unsold_flowers[plant.name] = len([p for p in self.plants if p.name == plant.name])
        sorted_unsold_flowers = sorted(unsold_flowers.items(), key=lambda kvp: (-kvp[1], kvp[0]))
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        orders = sum([c.total_orders for c in self.clients]) # TODO is there another way
        result = (f"~Flower Shop Report~\n"
                  f"Income: {self.income:.2f}\n"
                  f"Count of orders: {orders}\n"
                  f"~~Unsold plants: {sum(unsold_flowers.values())}~~\n")

        for plant_name, count in sorted_unsold_flowers:
            result += f"{plant_name}: {count}\n"

        result += f"~~Clients number: {len(sorted_clients)}~~\n"
        result += '\n'.join([c.client_details() for c in sorted_clients])
        return result

    def filter_clients_by_phone(self, phone_number) -> list[BaseClient]:
        return [
                client
                for client in self.clients
                if client.phone_number == phone_number
            ]