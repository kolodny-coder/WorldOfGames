from flask import Flask, render_template
# from redis import Redis/

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)



@app.route("/")
def score_server():
    try:
        with open('scores.txt') as f:
            scores = f.readlines()
            for score in scores:
                score = int(score)



        return render_template('scores_view.html', SCORE=score)
    except:
        return render_template('error_page.html', ERROR='Something Went Wrong')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')