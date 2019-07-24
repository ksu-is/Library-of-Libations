from flask import Flask, request, redirect, render_template
import sys
sys.path.insert(1, "PATH TO LOCAL PYTHON PACKAGES")  #OPTIONAL: Only if need to access Python packages installed on a local (non-global) directory
sys.path.insert(2, "PATH TO FLASK DIRECTORY")      #OPTIONAL: Only if you need to add the directory of your flask app

app = Flask(__name__)

@app.route('/') 
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'SELECT * FROM data_table'
    return render_template('sqldatabase.html', results=results, msg=msg)   
@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        drink_name = request.form['drink_name']
        spirit = request.form['spirit']
        ingredient_1 = request.form['ingredient_1']
        ingredient_2 = request.form['ingredient_2']
        ingredient_3 = request.form['ingredient_3']
        garnish = request.form['garnish']
        sql_edit_insert(''' INSERT INTO data_table (drink_name,spirit,ingredient_1,ingredient_2,ingredient_3,garnish) VALUES (?,?,?,?,?,?) ''', (drink_name,spirit,ingredient_1,ingredient_2,ingredient_3,garnish) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'INSERT INTO data_table (drink_name,spirit,ingredient_1,ingredient_2,ingredient_3,garnish) VALUES ('+drink_name+','+spirit+','+ingredient_1+','+ingredient_2+','+ingredient_3+','+garnish+')'
    return render_template('sqldatabase.html', results=results, msg=msg) 
@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        dname = request.args.get('dname')
        sql_delete(''' DELETE FROM data_table where drink_name = ?''', (dname) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'DELETE FROM data_table WHERE drink_name = ' + dname
    return render_template('sqldatabase.html', results=results, msg=msg)
@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        edname = request.args.get('edname')
        eresults = sql_query2(''' SELECT * FROM data_table where drink_name = ?''', (edname))
    results = sql_query(''' SELECT * FROM data_table''')
    return render_template('sqldatabase.html', eresults=eresults, results=results)
@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_drink_name = request.form['old_drink_name']
        spirit = request.form['spirit']
        drink_name = request.form['drink_name']
        ingredient_1 = request.form['ingredient_1']
        ingredient_2 = request.form['ingredient_2']
        ingredient_3 = request.form['ingredient_3']
        garnish = request.form['garnish']
        sql_edit_insert(''' UPDATE data_table set drink_name=?,spirit=?,ingredient_1=?,ingredient_2=?,ingredient_3=?,garnish=? WHERE drink_name=? and spirit=? ''', (drink_name,spirit,ingredient_1,ingredient_2,ingredient_3,garnish,old_drink_name) )
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'UPDATE data_table set drink_name = ' + drink_name + ', spirit = ' + spirit + ', ingredient_1 = ' + ingredient_1 + ', ingredient_2 = ' + ingredient_2 + ', ingredient_3 = ' + ingredient_3 + ', garnish = ' + garnish + ' WHERE drink_name = ' + old_drink_name
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)

