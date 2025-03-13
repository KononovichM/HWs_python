import xml.etree.ElementTree as ET


def calculate_total_cost(filename1):
    tree = ET.parse(filename1)
    root = tree.getroot()

    total_cost = 0
    for product in root.findall("product"):
        price = int(product.find("price").text)
        quantity = int(product.find("quantity").text)
        total_cost += price * quantity

    return total_cost


if __name__ == "__main__":
    filename = "products.xml"  # Имя XML-файла
    total = calculate_total_cost(filename)
    print(f"Общая стоимость всех товаров: {total} руб.")
