from flask import Flask, render_template, request,url_for, redirect

app=Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name="Smrity",
        is_topper=True,
        subjects=["Maths","Physics","Chemistry"]
        )



if __name__=="__main__":
    app.run(debug=True)
