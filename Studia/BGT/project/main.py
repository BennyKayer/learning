# Builtins
# import os

# 3rd party
from flask import Flask, render_template, redirect
from google.cloud import bigquery
# from google.cloud import storage
# import kaggle

# Local
from forms.survey_form import SurveyForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "@18*grn@xz28zo4yba6y^%_2=ibjn)sg-rpprlron=iibw6e-@"


@app.route("/")
def home():
    return render_template("pages/index.html")


@app.route("/tasks/update_dataset")
def cloud_tasks():
    # Can't make this work on standard
    # it needs access to root of the app engine instance
    # kaggle.api.authenticate()
    # kaggle.api.dataset_download_files('unsdsn/world-happiness',
    #                                   path="../data/",
    #                                   unzip=True)
    # kaggle.api.dataset_download_files('fernandol/countries-of-the-world',
    #                                   path="../data/",
    #                                   unzip=True)

    # storage_client = storage.Client()
    # bucket = storage_client.get_bucket("testing_kaggle_transfer")
    # for filename in os.listdir("../data"):
    #     blob = bucket.blob(filename)
    #     blob.upload_from_filename(os.path.join("../data", filename))

    return "Datasets Updated"


@app.route("/submit", methods=["POST", "GET"])
def submit():
    form = SurveyForm()
    if form.validate_on_submit():
        client = bigquery.Client()
        table = client.get_table("still-primer-271314.surveys.survey_2020")
        rows_to_insert = [(form.country.data,
                           form.economy.data,
                           form.freedom.data,
                           form.generosity.data,
                           form.healthcare.data,
                           form.overall_happiness.data,
                           form.social.data,
                           form.trustworthiness.data)]
        errors = client.insert_rows(table, rows_to_insert)
        if errors == []:
            return redirect("/thanks")
    else:
        return render_template("pages/submit.html", form=form)


@app.route("/sectors")
def gdp_sectors_composition():
    return render_template("pages/sectors.html")


@app.route("/mortality")
def mortality():
    return render_template("pages/mortality.html")


@app.route("/gdp_per_capita")
def gdp_per_capita():
    return render_template("pages/gdp_per_capita.html")


@app.route("/thanks")
def thanks_page():
    return render_template("pages/thanks_page.html")


if __name__ == "__main__":
    app.run(debug=True)
