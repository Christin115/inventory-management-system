import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"


def get_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    response = requests.get(
        url,
        headers={
            "User-Agent": "InventoryManagementSystem/1.0"
        },
        timeout=10
    )

    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("First 300 characters:")
    print(response.text[:300])

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except Exception:
        print("Response was not valid JSON.")
        return None

    if data.get("status") != 1:
        return None

    product = data["product"]

    return {
        "name": product.get("product_name", ""),
        "barcode": product.get("code", barcode),
        "brand": product.get("brands", ""),
        "category": product.get("categories", ""),
        "package_size": product.get("quantity", ""),
        "origin": product.get("origins", ""),
        "image_url": product.get("image_url", "")
    }