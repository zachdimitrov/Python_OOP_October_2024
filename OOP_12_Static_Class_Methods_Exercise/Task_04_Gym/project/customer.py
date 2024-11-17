class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.email = email
        self.address = address
        self.name = name
        self.id = self.get_next_id()
        Customer.id += 1

    @classmethod
    def get_next_id(cls):
        return cls.id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

