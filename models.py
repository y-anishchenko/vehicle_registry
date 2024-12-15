from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор
    registration_date = db.Column(db.Date, nullable=False)  # Дата регистрации
    vehicle_type = db.Column(db.String(50), nullable=False)  # Вид ТС
    make = db.Column(db.String(50), nullable=False)  # Марка
    model = db.Column(db.String(50), nullable=False)  # Модель
    vin_code = db.Column(db.String(17), unique=True, nullable=False)  # VIN-код
    frame_code = db.Column(db.String(50), nullable=True)  # Фрейм

    def __repr__(self):
        return f"<Vehicle {self.vin_code}>"
