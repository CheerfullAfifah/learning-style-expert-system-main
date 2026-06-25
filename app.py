import explanations

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    jsonify,
    make_response
)

from weasyprint import HTML

from dotenv import load_dotenv # type: ignore[import]

from questions import questions
from rules import (
    calculate_result
)

from inference import (
    forward_chaining
)

from models import db, Result
from recommendations import (
    recommendations,
    get_recommendations
)
from explanations import (
    generate_explanation,
    generate_analysis_extra
)

import os

load_dotenv()

app = Flask(__name__)

app.secret_key = 'learnstyle-secret-key'

print("DB_HOST =", os.getenv("DB_HOST"))
print("DB_NAME =", os.getenv("DB_NAME"))
print("DB_USER =", os.getenv("DB_USER"))
print("DB_PASSWORD =", os.getenv("DB_PASSWORD"))
print("DB_PORT =", os.getenv("DB_PORT"))

# CONFIG DATABASE POSTGRESQL
app.config['SQLALCHEMY_DATABASE_URI'] = (

    f"postgresql://"

    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"

)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# INIT DATABASE
db.init_app(app)


# CREATE TABLE
with app.app_context():
    db.create_all()


# HALAMAN UTAMA
@app.route('/')
def index():

    total_students = Result.query.count()

    visual_count = Result.query.filter_by(
        dominant='visual'
    ).count()

    auditory_count = Result.query.filter_by(
        dominant='auditory'
    ).count()

    kinesthetic_count = Result.query.filter_by(
        dominant='kinesthetic'
    ).count()

    dominant_data = {

        "visual": visual_count,

        "auditory": auditory_count,

        "kinesthetic": kinesthetic_count

    }

    if total_students == 0:

        most_dominant = "belum ada data"

    else:

        if total_students == 0:

            most_dominant = "belum ada data"

        else:

            most_dominant = max(

                dominant_data,

                key=dominant_data.get

            )

    insight_text = f"""
    Mayoritas siswa memiliki
    kecenderungan gaya belajar
    {most_dominant}.
    """

    return render_template(

        'index.html',
        questions=questions,
        total_students=total_students,
        visual_count=visual_count,
        auditory_count=auditory_count,
        kinesthetic_count=kinesthetic_count,
        insight_text=insight_text
    )

# HALAMAN START
@app.route('/start', methods=['GET', 'POST'])
def start():

    if request.method == 'POST':

        session['name'] = request.form['name']

        session['student_class'] = request.form['student_class']

        session['gender'] = request.form['gender']

        return redirect('/quiz')

    return render_template('start.html')

# HALAMAN QUIZ
@app.route('/quiz')
def quiz():

    return render_template(
        'quiz.html',
        questions=questions
    )


# HASIL QUIZ
@app.route('/result', methods=['POST'])
def result():

    facts = calculate_result(
        questions,
        request.form
    )

    fc_result = forward_chaining(
        facts
    )

    rule_trace = fc_result["rule_trace"]

    dominant = fc_result["goal"]

    visual_count = fc_result["visual_count"]

    auditory_count = fc_result["auditory_count"]

    kinesthetic_count = fc_result["kinesthetic_count"]

    total = (
        visual_count +
        auditory_count +
        kinesthetic_count
    )

    if total == 0:

        percentages = {
            "visual": 0,
            "auditory": 0,
            "kinesthetic": 0
        }

    else:

        percentages = {

            "visual": round(
                visual_count / total * 100,
                2
            ),

            "auditory": round(
                auditory_count / total * 100,
                2
            ),

            "kinesthetic": round(
                kinesthetic_count / total * 100,
                2
            )

        }

    explanation = generate_explanation(
        percentages
    )

    analysis_extra = generate_analysis_extra(
        percentages
    )

    recommendation_result = (
        get_recommendations(
            dominant,
            percentages
        )
    )

    new_result = Result(

        name=session['name'],

        student_class=session['student_class'],

        gender=session['gender'],

        visual=percentages['visual'],

        auditory=percentages['auditory'],

        kinesthetic=percentages['kinesthetic'],

        dominant=dominant

    )

    db.session.add(new_result)

    db.session.commit()

    return render_template(

        'result.html',

        dominant=dominant,

        percentages=percentages,

        recommendations=recommendation_result,

        explanation=explanation,

        name=session['name'],

        student_class=session['student_class'],

        gender=session['gender'],

        rule_trace=rule_trace,

        visual_count=visual_count,

        auditory_count=auditory_count,

        kinesthetic_count=kinesthetic_count,

        analysis_extra=analysis_extra,

    )

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():

    answers = request.get_json()

    if not answers:

        return jsonify({
            "error": "Data jawaban tidak ditemukan"
        }), 400

    print("\n===== ANSWERS =====")

    print(answers)

    print("===================\n")

    facts = calculate_result(

        questions,

        answers

    )

    fc_result = forward_chaining(

        facts

    )

    print("\n===== FC RESULT =====")

    print(fc_result)

    print("=====================\n")

    rule_trace = fc_result["rule_trace"]

    dominant = fc_result["goal"]

    visual_count = fc_result["visual_count"]

    auditory_count = fc_result["auditory_count"]

    kinesthetic_count = fc_result["kinesthetic_count"]

    total = (
        visual_count +
        auditory_count +
        kinesthetic_count
    )

    if total == 0:

        percentages = {

            "visual": 0,

            "auditory": 0,

            "kinesthetic": 0

        }

    else:

        percentages = {

            "visual": round(
                visual_count / total * 100,
                2
            ),

            "auditory": round(
                auditory_count / total * 100,
                2
            ),

            "kinesthetic": round(
                kinesthetic_count / total * 100,
                2
            )

        }

    explanation = generate_explanation(
        percentages
    )

    analysis_extra = generate_analysis_extra(
        percentages
    )

    recommendation_result = (
        get_recommendations(
            dominant,
            percentages
        )
    )

    new_result = Result(

        name=answers['name'],

        student_class=answers['student_class'],

        gender=answers['gender'],

        visual=percentages['visual'],

        auditory=percentages['auditory'],

        kinesthetic=percentages['kinesthetic'],

        dominant=dominant

    )

    db.session.add(new_result)

    db.session.commit()

    return jsonify({

        "dominant": dominant,

        "percentages": percentages,

        "recommendations": recommendation_result,

        "name": answers['name'],

        "student_class": answers['student_class'],

        "gender": answers['gender'],

        "explanation": explanation,

        "rule_trace": rule_trace,

        "visual_count": visual_count,

        "auditory_count": auditory_count,

        "kinesthetic_count": kinesthetic_count,

        "analysis_extra":
            analysis_extra,

    })

@app.route('/download-pdf', methods=['POST'])
def download_pdf():

    data = request.get_json()

    html = render_template(

        'cetak_pdf.html',

        name=data["name"],

        student_class=data["student_class"],

        gender=data["gender"],

        dominant=data["dominant"],

        percentages=data["percentages"],

        visual_count=data["visual_count"],

        auditory_count=data["auditory_count"],

        kinesthetic_count=data["kinesthetic_count"],

        explanation=data["explanation"],

        analysis_extra=data["analysis_extra"],

        rule_trace=data["rule_trace"],

        recommendations=data["recommendations"]

    )

    pdf = HTML(
        string=html
    ).write_pdf()

    response = make_response(pdf)

    response.headers[
        'Content-Type'
    ] = 'application/pdf'

    response.headers[
        'Content-Disposition'
    ] = (
        'attachment; '
        'filename=hasil-gaya-belajar.pdf'
    )

    return response

# DASHBOARD
@app.route('/dashboard')
def dashboard():

    results = Result.query.all()

    total_students = len(results)

    visual_count = len([
        r for r in results
        if r.dominant == 'visual'
    ])

    auditory_count = len([
        r for r in results
        if r.dominant == 'auditory'
    ])

    kinesthetic_count = len([
        r for r in results
        if r.dominant == 'kinesthetic'
    ])

    male_count = len([
        r for r in results
        if r.gender == 'Laki-laki'
    ])

    female_count = len([
        r for r in results
        if r.gender == 'Perempuan'
    ])
    dominant_data = {

        'visual': visual_count,

        'auditory': auditory_count,

        'kinesthetic': kinesthetic_count

    }

    most_dominant = max(

        dominant_data,

        key=dominant_data.get

    )

    if most_dominant == 'visual':

        insight = """

        Mayoritas siswa memiliki gaya belajar visual.
        Penggunaan video, diagram, warna,
        dan mind mapping dapat meningkatkan
        pemahaman siswa.

        """

    elif most_dominant == 'auditory':

        insight = """

        Mayoritas siswa memiliki gaya belajar auditori.
        Diskusi, penjelasan verbal,
        dan pembelajaran berbasis audio
        dapat membantu siswa memahami materi.

        """

    else:

        insight = """

        Mayoritas siswa memiliki gaya belajar kinestetik.
        Aktivitas praktik, simulasi,
        dan pembelajaran langsung sangat disarankan.

        """

    return render_template(

        'dashboard.html',

        results=results,

        total_students=total_students,

        visual_count=visual_count,

        auditory_count=auditory_count,

        kinesthetic_count=kinesthetic_count,

        male_count=male_count,

        female_count=female_count,

        insight=insight

    )

@app.route('/about')
def about():

    return render_template('about.html')

# RUN APP
if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )