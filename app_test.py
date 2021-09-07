from flask import Flask, render_template, url_for, request, redirect 
from src import scrape_sitemap60922

app = Flask(__name__)

def get_monthly_data(months):
    
    table=scrape_sitemap60922.df
    
    data = {
        "January": table,
        "February": "Second month of the year",
        "March": "Third month of the year",
        "April": 'IT WORKS',
        "May": "Fifth month of the year"
               
    }
    
    for k, v in data.items():
        if request.method=='POST':
            months=request.form.get('months')
        
            if k==months:
         
                return f'This is a value {k} and {table}'
            else:
  
                return data.get(months, "Data is not found")

@app.route('/tester', methods=['GET', 'POST'])
def tester():
    if request.method == "POST":
        months = request.form.get('months')
      
        return render_template('app_test_html.html', data = get_monthly_data(months), months=months)
     
    return render_template('app_test_html.html')

if __name__ == '__main__':
    app.run(debug = True)


