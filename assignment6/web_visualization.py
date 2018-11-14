from flask import Flask, render_template, request
import temperature_CO2_plotter as tp
from wtforms import SelectField

app = Flask(__name__)


@app.after_request
def disable_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route("/")
def main_menu():
    select = request.values.get('years_co2')
    print("2")
    print(str(select)) # just to see what select is
    return render_template('home.html', picture='static\co2.jpg')


#co2 plotting
@app.route('/plot_co2', methods=['POST'])
def draw_co2():
   year_from = int(request.form["year_from"])
   year_to = int(request.form["year_to"])

   y_min = int(request.form["min y-axis"])
   y_max = int(request.form["max y-axis"])

   if y_min > y_max or year_from > year_to:
      return view_co2()

   plot = tp.plot_CO2(year_from, year_to, y_min, y_max)
   plot.savefig("static\images\co2.png", dpi = 200)

   return view_co2(show = True)



@app.route('/plot_co2')
def view_co2(show=False):
   if show:
      return render_template("plot_co2.html", picture='\static\images\co2.png')
   else:
      return render_template("plot_co2.html", picture = "")


#temp plotting
@app.route('/plot_temp', methods=['POST'])
def draw_temp():
   year_from = int(request.form["year_from"])
   year_to = int(request.form["year_to"])

   month = request.form["month"]

   y_min = int(request.form["min y-axis"])
   y_max = int(request.form["max y-axis"])

   if y_min > y_max or year_from > year_to:
      return view_temp()

   plot = tp.plot_temperature(month, year_from, year_to, y_min, y_max)
   plot.savefig("static\images\\temp.png", dpi=200)

   return view_temp(show=True)


@app.route('/plot_temp')
def view_temp(show = False):
   if show:
      return render_template("plot_temp.html", picture='static\images\\temp.png')
   else:
      return render_template("plot_temp.html", picture="")


#co2  by country plotting
@app.route('/plot_co2_country', methods=['POST'])
def draw_co2_country():
   year_from = int(request.form["year_from"])
   year_to = int(request.form["year_to"])

   y_min = int(request.form["min y-axis"])
   y_max = int(request.form["max y-axis"])

   if y_min > y_max or year_from > year_to:
      return view_co2()

   plot = tp.plot_CO2(year_from, year_to, y_min, y_max)
   plot.savefig("static\images\co2.png", dpi=200)

   return view_co2(show=True)


@app.route('/plot_co2_country')
def view_co2_country(show=False):
   if show:
      return render_template("plot_co2_country.html", picture='\static\images\co2.png')
   else:
      return render_template("plot_co2_country.html", picture="")





if __name__ == "__main__":
    app.run(debug=True)



