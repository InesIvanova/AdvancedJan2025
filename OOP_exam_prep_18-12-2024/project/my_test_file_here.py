#Manager shop_report method6
import unittest
from project.flower_shop_manager import (FlowerShopManager)


class TestManagerMethod(unittest.TestCase):
    def setUp(self):
        self.manager = FlowerShopManager()

        self.manager.add_plant("Flower", "Rose", 10.0, 500, "Summer")
        self.manager.add_plant("Flower", "Rose", 10.0, 500, "Summer")
        self.manager.add_plant("Flower", "Tulip", 8.0, 400, "Spring")
        self.manager.add_plant("Flower", "Daisy", 5.0, 300, "Summer")
        self.manager.add_plant("LeafPlant", "Dracena", 4.0, 200, "M")

        self.manager.add_client("RegularClient", "Alice Smith", "1234567890")
        self.client1 = self.manager.clients[0]
        self.client1.total_orders = 2
        self.client1.discount = 5.0
        self.manager.add_client("RegularClient", "Bob Brown", "1122334455")
        self.client2 = self.manager.clients[1]
        self.client2.total_orders = 0
        self.client2.discount = 0.0
        self.manager.add_client("BusinessClient", "Greenhouse Inc", "2233445566")
        self.client3 = self.manager.clients[2]
        self.client3.total_orders = 5
        self.client3.discount = 10.0

        self.manager.income = 148.29


    def test_shop_report_no_unsold_plants__clients_order(self):
        self.manager.plants.clear()

        expected_report = (
"""~Flower Shop Report~
Income: 148.29
Count of orders: 7
~~Unsold plants: 0~~
~~Clients number: 3~~
Client: Greenhouse Inc, Phone number: 2233445566, Orders count: 5, Discount: 10%
Client: Alice Smith, Phone number: 1234567890, Orders count: 2, Discount: 5%
Client: Bob Brown, Phone number: 1122334455, Orders count: 0, Discount: 0%"""
        )

        actual_report = self.manager.shop_report()
        self.assertEqual(actual_report.strip(), expected_report)


if __name__ == '__main__':
    unittest.main()