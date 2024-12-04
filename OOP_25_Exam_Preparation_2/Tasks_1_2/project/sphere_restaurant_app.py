from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    WAITER_TYPES = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: list[BaseWaiter] = []
        self.clients: list[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."
        if waiter_name in [w.name for w in self.waiters]:
            return f"{waiter_name} is already on the staff."
        new_waiter = self.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."
        if client_name in [c.name for c in self.clients]:
            return f"{client_name} is already a client."
        new_client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        try:
            waiter = [w for w in self.waiters if w.name == waiter_name][0]
        except IndexError:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        try:
            client = [c for c in self.clients if c.name == client_name][0]
        except IndexError:
            return f"{client_name} is not a registered client."
        result = client.earning_points(order_amount)
        return f"{client_name} earned {result} points from the order."

    def apply_discount_to_client(self, client_name: str):
        try:
            client = [c for c in self.clients if c.name == client_name][0]
        except IndexError:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        percentage, remaining = client.apply_discount()
        return f"{client_name} received a {percentage}% discount. Remaining points {remaining}"

    def generate_report(self):
        result = "$$ Monthly Report $$\n"
        result += f"Total Earnings: ${sum([w.calculate_earnings() for w in self.waiters]):.2f}\n"
        result += f"Total Clients Unused Points: {sum([c.points for c in self.clients])}\n"
        result += f"Total Clients Count: {len(self.clients)}\n"

        result += "** Waiter Details **\n"
        sorted_waiters = sorted(self.waiters, key=lambda x: -x.calculate_earnings())
        result += "\n".join([str(w) for w in sorted_waiters])

        return result.strip()
