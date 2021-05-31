from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static_yu', static_folder='./static_yu')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yuting1101@localhost:3306/TESTDB'
db = SQLAlchemy(app)

class Staff(db.Model):
    __tablename__ = 'Staff'

    ID = db.Column(db.String(10), primary_key=True)
    Name = db.Column(db.String(10), nullable=False)
    DeptId = db.Column(db.String(10), nullable=False)
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(3))
    Salary = db.Column(db.Integer)
    RecordDt = db.Column(db.Date, nullable=False)

    # 這個類別被print出來會長什麼樣
    def __repr__(self):
        return "<User(name='%s', record='%s'>" % (self.Name, self.RecordDt)


@app.route('/show_staff')
def hello_google():
    staff_data = [[d.ID, d.Name, d.DeptId, str(d.Age), d.Gender, d.Salary] for d in db.session.query(Staff)]
    print(staff_data)
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)
# filter => 等於where
@app.route('/show_staff/<name>')
def show_staff(name):
    staff_data = [[d.ID, d.Name, d.DeptId, str(d.Age), d.Gender, d.Salary] for d in db.session.query(Staff).filter(Staff.Name == name)]
    print(staff_data)
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                           column=column)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)