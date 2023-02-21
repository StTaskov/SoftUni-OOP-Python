class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, DVD):
        if MovieWorld.dvd_capacity() > len(self.dvds):
            self.dvds.append(DVD)

    def rent_dvd(self, customer_id, dvd_id):

        needed_customer = None
        needed_dvd = None

        for customer in self.customers:
            if customer.id == customer_id:
                needed_customer = customer

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                needed_dvd = dvd

        if needed_dvd.id in [dvd.id for dvd in needed_customer.rented_dvds]:
            return f"{needed_customer.name} has already rented {needed_dvd.name}"

        if needed_dvd.is_rented:
            return f"DVD is already rented"

        if needed_customer.age < needed_dvd.age_restriction:
            return f"{needed_customer.name} should be at least {needed_dvd.age_restriction} to rent this movie"

        else:
            needed_dvd.is_rented = True
            needed_customer.rented_dvds.append(needed_dvd)
            return f"{needed_customer.name} has successfully rented {needed_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):

        needed_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        needed_customer = [customer for customer in self.customers if customer.id == customer_id][0]

        if needed_dvd in needed_customer.rented_dvds:
            needed_dvd.is_rented = False
            needed_customer.rented_dvds.remove(needed_dvd)
            return f"{needed_customer.name} has successfully returned {needed_dvd.name}"
        else:
            return f"{needed_customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += f"{repr(customer)}\n"
        for dvd in self.dvds:
            result += f"{repr(dvd)}\n"

        return result
