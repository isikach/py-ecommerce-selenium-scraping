from dataclasses import dataclass

from app.parse_class import ParseClass


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


pages = [
    None,
    "computers",
    "phones",
    "phones/touch",
    "computers/tablets",
    "computers/laptops"
]


def get_all_products() -> None:
    for page in pages:
        device = ParseClass(page)
        device.parse_processing()


if __name__ == "__main__":
    get_all_products()
