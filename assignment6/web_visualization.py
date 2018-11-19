from flask import Flask, render_template, request
import temperature_CO2_plotter as tp
from wtforms import SelectField

app = Flask(__name__)

# clears cache
@app.after_request
def disable_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route("/")
def main_menu():
   """
   Main menu.
   """
   select = request.values.get('years_co2')
   return render_template('home.html')


# co2 plotting
@app.route('/plot_co2', methods=['POST'])
def draw_co2():
   """
   Handles post requests for /plot_co2.
   Draws plots of CO2 levels over time, and saves the plot as a png file.
   Then renders and shows plot_co2.html

   Returns:
      template -- rendered template of co2.html
   """

   try:
      year_from = int(request.form["year_from"])
      year_to = int(request.form["year_to"])

      y_min = int(request.form["min y-axis"])
      y_max = int(request.form["max y-axis"])

      if y_min > y_max or year_from > year_to:
         return view_co2()

      plot = tp.plot_CO2(year_from, year_to, y_min, y_max)
      plot.savefig("static\images\co2.png", dpi = 600)

   except:
      return view_co2()

   return view_co2(show = True)


@app.route('/plot_co2')
def view_co2(show=False):
   """Shows a rendered page of of plot_co2.html.
   
   Keyword Arguments:
      show {bool} -- Flag, if set to True, it will show the plot (default: {False})
   
   Returns:
      template -- rendered template of co2.html
   """

   if show:
      return render_template("plot_co2.html", picture='\static\images\co2.png')
   else:
      return render_template("plot_co2.html", picture = "")



#temp plotting
@app.route('/plot_temp', methods=['POST'])
def draw_temp():
   """
   Handles post requests for /plot_temp.
   Draws plots of temperature over time, and saves the plot as a png file.
   Then renders and shows plot_temp.html


   Returns:
      template -- rendered template of plot_temp.html
   """

   # get form values
   try:
      year_from = int(request.form["year_from"])
      year_to = int(request.form["year_to"])

      month = request.form["month"]

      y_min = int(request.form["min y-axis"])
      y_max = int(request.form["max y-axis"])
   
      # if form values are invalig, reload page without plot
      if y_min > y_max or year_from > year_to:
         return view_temp()

      plot = tp.plot_temperature(month, year_from, year_to, y_min, y_max)
      plot.savefig("static\images\\temperature.png", dpi=600)
   
   except:
      return view_temp()
   
   return view_temp(show=True)


@app.route('/plot_temp')
def view_temp(show=False):
   """
   Handles GET requests for /plot_temp.
   Shows plots of temperature over time, and saves the plot as a png file.
   """
   if show:
      return render_template("plot_temp.html", picture='static\images\\temperature.png')
   else:
      return render_template("plot_temp.html", picture="")

@app.route('/documentation')
def show_documenation():
   return render_template('documentation.html')



#co2  by country plotting
@app.route('/plot_co2_country', methods=['POST'])
def draw_co2_country():
   """
   Handles post requests for /plot_temp.
   Draws plots of temperature over time, and saves the plot as a png file.
   """
   try:
      lower = float(request.form["lower"])
      upper = float(request.form["upper"])

      year = int(request.form["year"])
   
      # invalid input, render page without plot
      if lower > upper:
         return view_co2_country()
      
      plot = tp.plot_CO2_by_Country(lower, upper, year)
      plot.savefig("static\images\co2_country.png", dpi=600)

   except:
      return view_co2_country()

   return view_co2_country(show=True)


@app.route('/plot_co2_country')
def view_co2_country(show=False):
   """
   Handles GET requests for / plot_temp.
   Shows plots of temperature over time, and saves the plot as a png file.
   """
   if show:
      return render_template("plot_co2_country.html", picture='\static\images\co2_country.png')
   else:
      return render_template("plot_co2_country.html", picture="")



if __name__ == "__main__":
    app.run(debug=True)



