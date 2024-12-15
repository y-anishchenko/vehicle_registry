from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import db, Vehicle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Для flash сообщений
db.init_app(app)


@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return render_template('add_vehicle.html')


@app.route('/view')
def view_records():
    vehicles = Vehicle.query.all()  # Извлекаем все транспортные средства из базы данных
    return render_template('view_records.html', vehicles=vehicles)


@app.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    vin_code = request.form['vin_code']
    vehicle = Vehicle.query.filter_by(vin_code=vin_code).first()
    if vehicle:
        flash(f"Транспортное средство с VIN-кодом {vin_code} уже существует!", "danger")
        return redirect(url_for('home'))

    new_vehicle = Vehicle(
        registration_date=datetime.strptime(request.form['registration_date'], '%Y-%m-%d'),
        vehicle_type=request.form['vehicle_type'],
        make=request.form['make'],
        model=request.form['model'],
        vin_code=vin_code,
        frame_code=request.form['frame_code']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    flash("Транспортное средство успешно добавлено!", "success")
    return render_template('success.html', vehicle=new_vehicle)


if __name__ == '__main__':
    app.run(debug=True)
