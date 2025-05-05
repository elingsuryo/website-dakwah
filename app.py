from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Data tanya-jawab sesuai materi dakwah
dummy_qa = [
    {
        "question": "Apa hukum menggunakan agama untuk kepentingan pribadi?",
        "answer": "Menggunakan agama untuk kepentingan pribadi adalah perbuatan yang dilarang dalam Islam. Allah melarang menjual ayat-Nya demi kepentingan dunia, sebagaimana tercantum dalam Al-Qur'an, Surah Al-Baqarah: 41. Agama adalah untuk mendekatkan diri kepada Allah, bukan untuk meraih keuntungan duniawi."
    },
    {
        "question": "Bagaimana cara agar dakwah tidak tercampur dengan kepentingan pribadi?",
        "answer": "Agar dakwah tetap murni, niat harus diluruskan hanya untuk Allah semata, bukan untuk mendapatkan pujian atau materi. Rasulullah ﷺ bersabda bahwa ilmu yang dipelajari untuk dunia tidak akan mencium bau surga (HR. Abu Dawud, No. 3664)."
    },
    {
        "question": "Apa dampak buruk dari menyalahgunakan agama untuk kepentingan pribadi?",
        "answer": "Menyalahgunakan agama untuk kepentingan pribadi dapat menyesatkan umat, menciptakan ketidakadilan, dan merusak citra Islam. Allah melarang perbuatan ini dan menyebutnya sebagai bentuk kezaliman, sebagaimana disebutkan dalam Al-Qur'an, Surah Ash-Shaff: 7."
    },
    {
        "question": "Mengapa agama tidak boleh digunakan untuk tujuan duniawi?",
        "answer": "Agama adalah jalan hidup yang seharusnya membawa seseorang lebih dekat kepada Allah, bukan untuk mengejar keuntungan duniawi. Allah melarang umat-Nya untuk menjual ayat-Nya dan hukum-Nya demi keuntungan duniawi (Al-Qur'an, Surah Al-Baqarah: 41)."
    },
    {
        "question": "Bagaimana seharusnya seorang da'i menjaga niatnya?",
        "answer": "Seorang da'i harus menjaga niatnya dengan selalu mengingat bahwa dakwah adalah untuk menyampaikan kebenaran dan petunjuk Allah, bukan untuk mencari keuntungan pribadi atau pengakuan dari orang lain. Niat yang tulus akan membawa dakwah yang lebih berkah (Al-Qur'an, Surah Al-Isra: 80)."
    },
    {
        "question": "Apa yang dimaksud dengan ‘menjual agama untuk dunia’ dalam Islam?",
        "answer": "‘Menjual agama untuk dunia’ adalah tindakan menggunakan ajaran agama untuk mendapatkan keuntungan duniawi, seperti kekayaan, jabatan, atau ketenaran. Tindakan ini sangat dilarang dalam Islam karena mengaburkan tujuan utama agama (Al-Qur'an, Surah Al-Baqarah: 41)."
    },
    {
        "question": "Apa yang terjadi jika seseorang menggunakan agama untuk keuntungan pribadi?",
        "answer": "Menggunakan agama untuk keuntungan pribadi dapat mengarah pada perbuatan nifaq (hipokrit) dan dapat merusak hubungan dengan Allah dan umat. Islam mengajarkan agar setiap amalan dilakukan dengan ikhlas hanya karena Allah (Al-Qur'an, Surah Al-Bayyinah: 5)."
    },
    {
        "question": "Bagaimana cara menghindari godaan untuk menggunakan agama demi kepentingan pribadi?",
        "answer": "Untuk menghindari godaan ini, seseorang harus memperkuat iman, selalu introspeksi diri, dan menjaga keikhlasan dalam setiap tindakan. Selain itu, penting untuk mendekatkan diri kepada Allah dengan doa dan dzikir (Al-Qur'an, Surah Al-Ankabut: 45)."
    },
    {
        "question": "Apa yang seharusnya menjadi tujuan utama dakwah dalam Islam?",
        "answer": "Tujuan utama dakwah dalam Islam adalah untuk menyampaikan wahyu Allah kepada umat manusia agar mereka mendapatkan petunjuk dan rahmat-Nya. Dakwah tidak boleh bertujuan untuk mendapatkan keuntungan pribadi (Al-Qur'an, Surah An-Nahl: 125)."
    },
    {
        "question": "Apa hukumnya memanfaatkan ajaran agama untuk menarik massa atau pengikut?",
        "answer": "Memanfaatkan ajaran agama untuk menarik massa atau pengikut demi kepentingan pribadi adalah perbuatan yang tercela dalam Islam. Dakwah harus dilaksanakan dengan tujuan semata-mata untuk mendapatkan ridha Allah (Al-Qur'an, Surah Al-Kahf: 28)."
    },
    {
        "question": "Apa konsekuensi spiritual dari menggunakan agama untuk kepentingan pribadi?",
        "answer": "Menggunakan agama untuk kepentingan pribadi dapat menyebabkan hilangnya keberkahan dalam amal, menjauhkan diri dari rahmat Allah, dan mengundang azab di akhirat (Al-Qur'an, Surah Al-Munafiqun: 9)."
    },
    {
        "question": "Bagaimana cara mengetahui apakah dakwah seseorang murni atau untuk kepentingan pribadi?",
        "answer": "Dakwah yang murni ditandai dengan keikhlasan, tidak mencari pujian atau imbalan duniawi, dan berfokus pada kebenaran. Jika dakwah diwarnai dengan ambisi pribadi, seperti mencari kekayaan atau popularitas, maka itu tidak murni (HR. Muslim, No. 1905)."
    },
    {
        "question": "Apa yang harus dilakukan jika melihat seseorang menyalahgunakan agama untuk kepentingan pribadi?",
        "answer": "Seorang Muslim harus menasihati dengan lembut, mengingatkan tentang pentingnya keikhlasan, dan jika perlu, melaporkan kepada pihak berwenang jika tindakan tersebut merugikan masyarakat (Al-Qur'an, Surah Al-Asr: 3)."
    },
    {
        "question": "Bagaimana Islam memandang orang yang memanfaatkan agama untuk politik?",
        "answer": "Islam melarang penggunaan agama untuk kepentingan politik yang bertujuan pribadi atau kelompok, karena ini dapat memecah belah umat dan menodai kesucian agama (Al-Qur'an, Surah Al-Ma’idah: 2)."
    },
    {
        "question": "Apa peran keikhlasan dalam menjaga kemurnian dakwah?",
        "answer": "Keikhlasan adalah kunci utama dalam dakwah. Tanpa keikhlasan, dakwah bisa tercampur dengan kepentingan pribadi, sehingga kehilangan nilai ibadah dan keberkahan (Al-Qur'an, Surah Az-Zumar: 2)."
    },
    {
        "question": "Bagaimana cara melatih diri untuk selalu ikhlas dalam berdakwah?",
        "answer": "Melatih keikhlasan dapat dilakukan dengan memperbanyak muhasabah (introspeksi), berdoa memohon keikhlasan, dan mengingat bahwa segala amal hanya untuk Allah (HR. Bukhari, No. 6502)."
    },
    {
        "question": "Apa hukum menerima imbalan materi dari dakwah?",
        "answer": "Menerima imbalan materi dari dakwah diperbolehkan jika tidak menjadi tujuan utama dan sesuai dengan kebutuhan hidup, tetapi dakwah harus tetap dilakukan dengan ikhlas untuk Allah (Al-Qur'an, Surah Asy-Syarh: 6)."
    },
    {
        "question": "Mengapa menjaga keikhlasan dalam dakwah sangat sulit?",
        "answer": "Menjaga keikhlasan sulit karena godaan duniawi, seperti pujian, kekayaan, atau popularitas, sering kali menggoda hati. Oleh karena itu, seorang da’i perlu terus memperkuat iman dan muhasabah (Al-Qur'an, Surah Al-Hadid: 20)."
    },
    {
        "question": "Apa yang dimaksud dengan nifaq dalam konteks menyalahgunakan agama?",
        "answer": "Nifaq adalah sikap munafik, yaitu menunjukkan keimanan di depan orang lain tetapi sebenarnya menggunakan agama untuk kepentingan pribadi, yang sangat dicela dalam Islam (Al-Qur'an, Surah Al-Munafiqun: 1)."
    },
    {
        "question": "Bagaimana cara membedakan dakwah yang tulus dengan yang bertujuan duniawi?",
        "answer": "Dakwah yang tulus berfokus pada kebenaran, tidak mencari imbalan duniawi, dan dilakukan dengan rendah hati. Sebaliknya, dakwah duniawi sering kali mencari popularitas atau keuntungan materi (HR. Tirmidzi, No. 265)."
    },
    {
        "question": "Apa hubungan antara riya dan menyalahgunakan agama?",
        "answer": "Riya adalah perbuatan mencari pujian manusia dalam ibadah, termasuk dakwah. Ini adalah bentuk penyalahgunaan agama karena tujuannya bukan untuk Allah, melainkan pengakuan duniawi (HR. Muslim, No. 2986)."
    },
    {
        "question": "Bagaimana cara mengenali tanda-tanda riya dalam dakwah?",
        "answer": "Tanda-tanda riya dalam dakwah meliputi keinginan untuk dipuji, merasa senang ketika diakui, atau kecewa ketika usaha dakwah tidak dihargai manusia (Al-Qur'an, Surah Al-Insyirah: 7)."
    },
    {
        "question": "Apa nasihat Rasulullah tentang menjaga keikhlasan dalam amal?",
        "answer": "Rasulullah ﷺ mengajarkan bahwa amal yang diterima Allah adalah yang dilakukan dengan ikhlas dan sesuai dengan syariat. Beliau memperingatkan agar tidak mencari pujian manusia (HR. Muslim, No. 1905)."
    },
    {
        "question": "Bagaimana cara menasihati seseorang yang menggunakan agama untuk kepentingan pribadi?",
        "answer": "Nasehat harus diberikan dengan lembut, penuh hikmah, dan berfokus pada pentingnya keikhlasan serta akibat buruk dari perbuatan tersebut di dunia dan akhirat (Al-Qur'an, Surah An-Nahl: 125)."
    },
    {
        "question": "Apa yang bisa dilakukan masyarakat untuk mencegah penyalahgunaan agama?",
        "answer": "Masyarakat dapat meningkatkan literasi agama, memilih pemimpin atau da’i yang tulus, and melaporkan penyalahgunaan agama kepada otoritas yang berwenang (Al-Qur'an, Surah Al-Hujurat: 6)."
    },
    {
        "question": "Bagaimana cara mendeteksi motif tersembunyi dalam dakwah seseorang?",
        "answer": "Motif tersembunyi dapat dideteksi dengan melihat apakah dakwah tersebut lebih mengutamakan kepentingan pribadi, seperti kekayaan atau kekuasaan, daripada kebenaran dan kesejahteraan umat (Al-Qur'an, Surah Al-Kahf: 28)."
    },
    {
        "question": "Apa hukum memanfaatkan ayat Al-Qur’an untuk kampanye pribadi?",
        "answer": "Memanfaatkan ayat Al-Qur’an untuk kampanye pribadi yang bertujuan duniawi adalah haram, karena ini termasuk menjual ayat Allah untuk keuntungan pribadi (Al-Qur'an, Surah Al-Baqarah: 41)."
    },
    {
        "question": "Bagaimana cara menjaga hati dari godaan duniawi saat berdakwah?",
        "answer": "Menjaga hati dari godaan duniawi dapat dilakukan dengan memperbanyak dzikir, berdoa memohon perlindungan dari Allah, dan selalu mengingat tujuan akhirat (Al-Qur'an, Surah Ar-Ra’d: 28)."
    },
    {
        "question": "Apa peran doa dalam menjaga keikhlasan dakwah?",
        "answer": "Doa membantu seorang da’i untuk memohon keikhlasan, keteguhan hati, dan perlindungan dari godaan duniawi, sehingga dakwah tetap murni untuk Allah (Al-Qur'an, Surah Al-Furqan: 65)."
    },
    {
        "question": "Bagaimana cara memastikan dakwah tidak menjadi alat untuk mencari popularitas?",
        "answer": "Untuk menghindari popularitas, seorang da’i harus fokus pada keikhlasan, menghindari sorotan publik yang tidak perlu, dan selalu memeriksa niatnya sebelum berdakwah (HR. Bukhari, No. 6492)."
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question'].lower().strip().rstrip('?')
    answer = "Maaf, pertanyaan Anda belum bisa dijawab oleh sistem."

    # Pencocokan case-insensitive dan tanpa memerlukan tanda tanya
    for qa in dummy_qa:
        if qa["question"].lower().strip().rstrip('?') == question:
            answer = qa["answer"]
            break

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)