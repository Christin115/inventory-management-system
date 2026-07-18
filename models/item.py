from models import db


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), nullable=False)
    barcode = db.Column(db.String(50), unique=True)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(200))
    package_size = db.Column(db.String(50))
    origin = db.Column(db.String(100))
    image_url = db.Column(db.String(500))

    quantity = db.Column(db.Integer, default=1)
    price = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "barcode": self.barcode,
            "brand": self.brand,
            "category": self.category,
            "package_size": self.package_size,
            "origin": self.origin,
            "image_url": self.image_url,
            "quantity": self.quantity,
            "price": self.price
        }