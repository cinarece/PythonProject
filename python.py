from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Anasayfa
@app.route('/')
def home():
    return render_template('home.html')


# Giriş sayfası
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']

        # Şifreyi kontrol et
        if password == 'Holland':
            return redirect(url_for('welcome'))  # Başarıyla giriş
        else:
            return render_template('login.html', error="Üzgünüm, yanlış şifre girdiniz.")  # Hata mesajı
    return render_template('login.html')


# Hoş geldin sayfası
@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        # Anket cevaplarını al
        cevaplar = {
            '1': request.form.get('q1'),
            '2': request.form.get('q2'),
            '3': request.form.get('q3'),
            '4': request.form.get('q4'),
            '5': request.form.get('q5'),
            '6': request.form.get('q6'),
            '7': request.form.get('q7'),
            '8': request.form.get('q8'),
            '9': request.form.get('q9'),
            '10': request.form.get('q10'),
            '11': request.form.get('q11'),
            '12': request.form.get('q12'),
            '13': request.form.get('q13'),
            '14': request.form.get('q14'),
            '15': request.form.get('q15'),
            '16': request.form.get('q16'),
            '17': request.form.get('q17'),
            '18': request.form.get('q18'),
            '19': request.form.get('q19'),
            '20': request.form.get('q20'),
            '21': request.form.get('q21'),
            '22': request.form.get('q22'),
            '23': request.form.get('q23'),
            '24': request.form.get('q24'),
            '25': request.form.get('q25'),
            '26': request.form.get('q26'),
            '27': request.form.get('q27'),
            '28': request.form.get('q28'),
            '29': request.form.get('q29'),
            '30': request.form.get('q30'),
            '31': request.form.get('q31'),
            '32': request.form.get('q32'),
            '33': request.form.get('q33'),
            '34': request.form.get('q34'),
            '35': request.form.get('q35'),
            '36': request.form.get('q36'),
            '37': request.form.get('q37'),
            '38': request.form.get('q38'),
            '39': request.form.get('q39'),
            '40': request.form.get('q40'),
            '41': request.form.get('q41'),
            '42': request.form.get('q42'),
            '43': request.form.get('q43'),
            '44': request.form.get('q44'),
            '45': request.form.get('q45'),
            '46': request.form.get('q46'),
            '47': request.form.get('q47'),
            '48': request.form.get('q48'),
            '49': request.form.get('q49'),
            '50': request.form.get('q50'),
            '51': request.form.get('q51'),
            '52': request.form.get('q52'),
            '53': request.form.get('q53'),
            '54': request.form.get('q54'),
            '55': request.form.get('q55'),
            '56': request.form.get('q56'),
            '57': request.form.get('q57'),
            '58': request.form.get('q58'),
            '59': request.form.get('q59'),
            '60': request.form.get('q60'),
            '61': request.form.get('q61'),
            '62': request.form.get('q62'),
            '63': request.form.get('q63'),
            '64': request.form.get('q64'),
            '65': request.form.get('q65'),
            '66': request.form.get('q66'),
            '67': request.form.get('q67'),
            '68': request.form.get('q68'),
            '69': request.form.get('q69'),
            '70': request.form.get('q70'),
            '71': request.form.get('q71'),
            '72': request.form.get('q72'),
            '73': request.form.get('q73'),
            '74': request.form.get('q74'),
            '75': request.form.get('q75'),
            '76': request.form.get('q76'),
            '77': request.form.get('q77'),
            '78': request.form.get('q78'),
            '79': request.form.get('q79'),
            '80': request.form.get('q80'),
            '81': request.form.get('q81'),
            '82': request.form.get('q82'),
            '83': request.form.get('q83'),
            '84': request.form.get('q84'),
            '85': request.form.get('q85'),
            '86': request.form.get('q86'),
            '87': request.form.get('q87'),
            '88': request.form.get('q88'),
            '89': request.form.get('q89'),
            '90': request.form.get('q90'),
        }


        sonuc = {
            'Araştırıcı': 0,
            'Sanatsal': 0,
            'Sosyal': 0,
            'Girişimci': 0,
            'Geleneksel': 0,
            'Gerçekçi': 0,
        }

        for key, value in cevaplar.items():
            if value == 'hoşlanmam':
                sonuc['Araştırıcı'] += 1
            elif value == 'fark etmez':
                sonuc['Sosyal'] += 1
            elif value == 'hoşlanırım':
                sonuc['Girişimci'] += 1

        # En yüksek puanı alana göre meslek önerisi yapacağız
        en_uygun_meslek = max(sonuc, key=sonuc.get)

        return render_template('anket_sonuc.html', sonuc=sonuc, en_uygun_meslek=en_uygun_meslek)

    return render_template('welcome.html')



if __name__ == "__main__":
    app.run(debug=True)
