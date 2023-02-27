from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/WS/')
def WS():
    return render_template("WS.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/MC/')
def MC():
    return render_template("MC.html")

@app_projects.route('/MGUN/')
def MGUN():
    return render_template("MGUN.html")

@app_projects.route('/AP/')
def AP():
    return render_template("AP.html")

@app_projects.route('/GAS/')
def GAS():
    return render_template("GAS.html")