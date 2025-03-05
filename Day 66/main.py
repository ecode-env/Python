import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

    #     # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
    #     return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def get_random_cafe():

    random_cafe = random.choice(Cafe.query.all())
    return jsonify(cafe=random_cafe.to_dict())
    # return jsonify(
    #     cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })
    # return jsonify(cafe={
    #     # Omit the id from the response
    #     # "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #
    #     # Put some properties in a sub-category
    #     "amenities": {
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #     }
    # })

# To get all caffes

@app.route('/all')
def get_all_cafes():
    # all_cafes = []
    # for cafe in Cafe.query.all():
    #     all_cafes.append({
    #         "id": cafe.id,
    #         "name": cafe.name,
    #         "map_url": cafe.map_url,
    #         "img_url": cafe.img_url,
    #         "location": cafe.location,
    #         "seats": cafe.seats,
    #         "has_toilet": cafe.has_toilet,
    #         "has_wifi": cafe.has_wifi,
    #         "has_sockets": cafe.has_sockets,
    #         "can_take_calls": cafe.can_take_calls,
    #         "coffee_price": cafe.coffee_price,
    #     })
    #
    # return jsonify(cafe=all_cafes)

    all_cafes = Cafe.query.all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])

@app.route('/search')
def search():

    key = request.args.get('loc')
    location = Cafe.query.filter(Cafe.location == key).all()

    if location:
        return jsonify(cafe=[cafe.to_dict() for cafe in location])

    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})



# HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_new_cafe():

    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "success": "Successfully added the new cafe."
    })

# HTTP PUT/PATCH - Update Record



# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
