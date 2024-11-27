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
            # Tüm sorular için aynı şekilde devam et
        }

        # Meslek gruplarına göre puan hesaplama
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
