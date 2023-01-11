from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discount: int
    category: str

    def get_final_price(self):
        return self.price * (100 - self.discount) / 100
        # return self.price - self.price * self.discount / 100

    def __hash__(self):
        return hash(self.name) + hash(self.price) + hash(self.discount) + hash(self.category)


if __name__ == '__main__':
    p1 = Product('Bere', 3.0, 0, '')
    p2 = Product('Bere', 3.0, 0, '')

    s = set()
    s.add(p1)
    s.add(p2)

    print(s)
