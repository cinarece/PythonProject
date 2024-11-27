function hesaplaSonuc() {
    // Meslek puanlarını sıfırla
    let meslekPuanlari = {
        "Araştırıcı": 0,
        "Sanatsal": 0,
        "Sosyal": 0,
        "Girişimci": 0,
        "Geleneksel": 0,
        "Gerçekçi": 0
    };

    // Anket formundaki tüm cevapları kontrol et
    let form = document.forms['anketForm'];
    for (let i = 0; i < form.length; i++) {
        let secim = form[i];
        if (secim.checked) {
            // "Hoşlanırım" cevabı için uygun puanlama
            if (secim.value === "Hoşlanırım") {
                if (secim.name === "q3") {
                    meslekPuanlari["Gerçekçi"]++; // Hava durumu sorusunu Gerçekçi grubuna ekleyin
                } else if (secim.name === "q1") {
                    meslekPuanlari["Araştırıcı"]++; // Bilimsel araştırma için Araştırıcı
                }
                // Diğer soruları burada değerlendirebilirsiniz
            }
        }
    }

    // Sonuçları hesaplama ve gösterme işlemi
    let sonucListe = document.getElementById("sonuclar");
    sonucListe.innerHTML = ''; // Önceki sonuçları temizle
    for (let meslek in meslekPuanlari) {
        let li = document.createElement("li");
        li.innerHTML = `<strong>${meslek}</strong>: ${meslekPuanlari[meslek]} puan`;
        sonucListe.appendChild(li);
    }

    let enUygunMeslek = Object.keys(meslekPuanlari).reduce((a, b) => meslekPuanlari[a] > meslekPuanlari[b] ? a : b);
    document.getElementById("en-uygun-meslek").textContent = enUygunMeslek;
}
