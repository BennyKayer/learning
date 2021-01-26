from google.cloud import firestore
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    db = firestore.Client()
    jobs_ref = db.collection('jobs')
    jobs_dicts = [x.to_dict() for x in jobs_ref.stream()]

    return render_template('./jobs.html', jobs=jobs_dicts)


@app.route('/job', methods=["POST"])
def add_job():
    db = firestore.Client()
    request_data = request.get_json()

    doc_ref = db.collection('jobs').document(request_data["Title"])
    try:
        new_job = {
            "Title": request_data["Title"],
            "Company": request_data["Company"],
            "Category": request_data["Category"],
            "Location": request_data["Location"],
            "Responsibilities": request_data["Responsibilities"],
            "Minimum Qualification": request_data["Minimum Qualification"],
            "Preferred Qualification": request_data["Preferred Qualification"]
        }
    except KeyError:
        message = {"message": "Wrong request body"}
        return jsonify(message), 400

    doc_ref.set(new_job)
    return jsonify(new_job), 200


@app.route("/jobs", methods=["GET"])
def get_jobs():
    db = firestore.Client()
    jobs_ref = db.collection('jobs')
    jobs_dicts = [x.to_dict() for x in jobs_ref.stream()]

    return jsonify(jobs_dicts), 200


@app.route("/trigger")
def trigger():
    cloud_config = {"app_engine_http_request": {
            "http_method": "POST",
            "relative_uri": "/cloud_tasks"
        }}
    return cloud_config, 200
# laboratorium-1-s16569 europe-west q1


@app.route("/cloud_tasks")
def cloud_tasks():
    return "Hello Worker", 200


@app.route('/hello')
def main():
    # # Add a new document
    # db = firestore.Client()
    # doc_ref = db.collection(u'users').document(u'alovelace')
    # doc_ref.set({
    #     u'first': u'Ada',
    #     u'last': u'Lovelace',
    #     u'born': 1815
    # })

    # # Then query for documents
    # users_ref = db.collection(u'users')

    # for doc in users_ref.stream():
    #     print(u'{} => {}'.format(doc.id, doc.to_dict()))

    return "Hello BGT"


if __name__ == "__main__":
    app.run(debug=True)
