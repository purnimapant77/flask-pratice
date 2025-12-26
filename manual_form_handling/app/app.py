from flask import Flask ,render_template, request,redirect,url_for,flash
app=Flask(__name__)

@app.route("/")
def send_to_feedback():
    return redirect(url_for("feedback"))

@app.route("/feedback",methods=["GET","POST"])
def feedback():
    if request.method=="POST":
        #name=request.form['name']   (this method returns error if their is null value)
        #message=request.form['message']
        name=request.form.get("username")   #get is safer method as if their is no value it gives null
        message=request.form.get("message")
        return render_template("thankyou.html",user=name,message=message)
    
    return render_template("feedback.html")


if __name__=="__main__":
    app.run(debug=True)
