from flask import Flask, render_template, request
import string

app = Flask(__name__)

# ---------- PASSWORD LOGIC ----------
def analyze_password(password):
    score = 0
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char.isdigit():
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if len(password) >= 8: score += 1
    if lower_count > 0: score += 1
    if upper_count > 0: score += 1
    if num_count > 0: score += 1
    if special_count > 0: score += 1

    if score <= 3:
        remarks = "Weak password"
    elif score == 4:
        remarks = "Good password"
    else:
        remarks = "Very strong password"

    return {
        "score": score,
        "remarks": remarks
    }

# ---------- ROUTE ----------
@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form["password"]
        result = analyze_password(password)

    return render_template("index.html", result=result)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
