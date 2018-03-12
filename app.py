from flask import Flask, render_template, flash, request, Markup, send_from_directory
from wtforms import Form, IntegerField, TextField, TextAreaField, validators, StringField, SubmitField
from worktime import generate_xlsx_result

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    year = IntegerField('Year (e.g. 2018):', validators=[validators.required()])
    month = IntegerField('Month (e.g. 2):', validators=[validators.required()])
    name = TextField('Name (e.g. Tony Tony Chopper ):', validators=[validators.required()])
    number = IntegerField('Number (e.g. 10):', validators=[validators.required()])
    
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    if request.method == 'POST':
        year=request.form['year']
        month=request.form['month']
        name=request.form['name']
        number=request.form['number']

        file_name = year + '-' + month + '-' + name + '.xlsx'
 
        if form.validate():
            # Save the comment here.
            flash(Markup('報表已經產生: <a href="xlsx/') + file_name + Markup('" class="alert-link">here</a>'))
        generate_xlsx_result(int(year), int(month), name, int(number))
 
    return render_template('index.html', form=form)

@app.route('/xlsx/<path:path>')
def send_js(path):
    return send_from_directory('xlsx', path)



if __name__ == "__main__":
    app.run()