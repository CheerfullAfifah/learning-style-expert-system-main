recommendations = {

    "visual": {

        "student": [

            "Gunakan mind mapping, diagram, atau warna untuk membantu memahami dan mengingat materi.",
            
            "Video pembelajaran dan visualisasi materi dapat membantu meningkatkan fokus belajar.",
            
            "Buat rangkuman visual agar materi lebih mudah dipahami dan diingat kembali.",
            
            "Gunakan catatan yang terstruktur dan menarik secara visual untuk membantu proses belajar mandiri.",
            
            "Hindari belajar dengan teks yang terlalu panjang tanpa bantuan visual pendukung.",

        ],

        "teacher": [

            "Gunakan media visual seperti gambar, diagram, video, atau slide interaktif saat pembelajaran.",
            
            "Tuliskan poin penting secara terstruktur agar siswa lebih mudah memahami materi.",
            
            "Kombinasikan penjelasan dengan ilustrasi visual untuk meningkatkan fokus belajar siswa.",
            
            "Gunakan warna atau penekanan visual pada konsep penting agar materi lebih mudah diingat.",
            
            "Berikan contoh konkret dan visualisasi materi agar siswa lebih cepat memahami pembelajaran.",

        ],

        "parent": [

            "Berikan dukungan belajar menggunakan media visual seperti video edukasi atau buku bergambar.",
            
            "Bantu anak membuat rangkuman atau catatan visual agar materi lebih mudah dipahami.",
            
            "Ciptakan lingkungan belajar yang rapi dan nyaman agar anak lebih fokus belajar.",
            
            "Dukung anak menggunakan metode belajar kreatif seperti mind mapping atau flashcard.",
            
            "Hindari terlalu banyak instruksi verbal tanpa bantuan visual pendukung.",

        ]

    },

    "auditory": {

        "student": [

            "Belajar melalui diskusi dan penjelasan verbal dapat membantu meningkatkan pemahaman materi.",
            
            "Cobalah menjelaskan kembali materi dengan berbicara agar informasi lebih mudah diingat.",
            
            "Gunakan rekaman suara, podcast edukasi, atau video penjelasan sebagai media belajar tambahan.",
            
            "Belajar bersama teman dapat membantu menjaga fokus dan memperkuat pemahaman.",
            
            "Diskusi aktif dan tanya jawab biasanya lebih efektif dibanding hanya membaca materi sendiri.",

        ],

        "teacher": [

            "Gunakan penjelasan verbal yang jelas dan interaktif selama pembelajaran.",
            
            "Berikan kesempatan siswa untuk bertanya dan berdiskusi secara aktif.",
            
            "Kombinasikan pembelajaran dengan presentasi, diskusi kelompok, atau tanya jawab.",
            
            "Hindari pembelajaran yang terlalu pasif tanpa komunikasi dua arah.",
            
            "Gunakan intonasi dan komunikasi aktif untuk membantu menjaga perhatian siswa."

        ],

        "parent": [

            "Ajak anak berdiskusi mengenai materi yang dipelajari di sekolah.",
            
            "Dengarkan anak menjelaskan kembali pelajaran untuk membantu memperkuat pemahaman.",
            
            "Dukung anak belajar menggunakan audio pembelajaran atau video penjelasan.",
            
            "Berikan kesempatan anak belajar bersama teman agar proses belajar lebih nyaman.",
            
            "Hindari memaksa anak belajar terlalu lama secara diam tanpa interaksi.",

        ]

    },

    "kinesthetic": {

        "student": [

            "Gunakan aktivitas praktik langsung agar fokus belajar tetap terjaga.",

            "Belajar melalui simulasi, eksperimen, atau project sederhana dapat membantu meningkatkan pemahaman materi.",

            "Hindari belajar terlalu lama tanpa aktivitas karena dapat menyebabkan kehilangan fokus.",

            "Gunakan metode belajar aktif seperti roleplay, demonstrasi, atau praktik mandiri.",
            
            "Belajar sambil melakukan aktivitas ringan dapat membantu menjaga konsentrasi belajar.",

        ],

        "teacher": [

            "Berikan aktivitas praktik atau simulasi agar siswa tetap terlibat selama pembelajaran.",
            
            "Hindari metode ceramah terlalu lama karena siswa kinestetik cenderung cepat kehilangan fokus.",
            
            "Gunakan pembelajaran berbasis aktivitas, eksperimen, atau project sederhana.",
            
            "Berikan kesempatan siswa untuk bergerak dan berinteraksi selama proses belajar.",
            
            "Kombinasikan pembelajaran dengan praktik langsung agar siswa lebih mudah memahami materi.",

        ],

        "parent": [

            "Berikan aktivitas belajar yang melibatkan praktik langsung di rumah.",
            
            "Hindari memaksa anak belajar terlalu lama hanya dengan membaca atau mendengarkan.",
            
            "Dukung anak belajar melalui aktivitas interaktif dan pengalaman nyata.",
            
            "Bantu anak menjaga fokus belajar dengan selingan aktivitas ringan.",
            
            "Gunakan permainan edukatif atau aktivitas praktik sederhana untuk membantu proses belajar.",

        ]
    },

    "campuran": {

        "student": [

            "Gunakan kombinasi gambar, diskusi, dan praktik langsung saat belajar.",

            "Cobalah berbagai metode belajar untuk menemukan cara yang paling efektif.",

            "Manfaatkan media visual, audio, dan aktivitas praktik secara seimbang."

        ],

        "teacher": [

            "Gunakan pendekatan pembelajaran yang bervariasi.",

            "Kombinasikan presentasi visual, diskusi kelas, dan kegiatan praktik.",

            "Berikan variasi metode penyampaian materi."

        ],

        "parent": [

            "Dukung anak dengan berbagai cara belajar di rumah.",

            "Sediakan media belajar visual, audio, dan praktik.",

            "Amati metode belajar yang paling efektif bagi anak."

        ]

    },

}

def get_recommendations(
    dominant,
    percentages
):

    visual = percentages["visual"]

    auditory = percentages["auditory"]

    kinesthetic = percentages["kinesthetic"]

    sorted_scores = sorted(

        percentages.items(),

        key=lambda x: x[1],

        reverse=True

    )

    primary = sorted_scores[0][0]

    secondary = sorted_scores[1][0]

    difference = (
        sorted_scores[0][1]
        -
        sorted_scores[1][1]
    )

    base = recommendations.get(
        dominant,
        recommendations["visual"]
    )

    student = base["student"][:]

    teacher = base["teacher"][:]

    parent = base["parent"][:]

    # =========================================
    # BALANCED LEARNING STYLE
    # =========================================

    if difference <= 5:

        student.append(
            f"Anda memiliki keseimbangan gaya belajar {primary} dan {secondary}. Gunakan kombinasi beberapa metode belajar agar pemahaman lebih optimal."
        )

        teacher.append(
            "Gunakan pendekatan pembelajaran yang bervariasi karena siswa mampu memahami materi melalui lebih dari satu metode belajar."
        )

        parent.append(
            "Berikan variasi metode belajar di rumah agar kemampuan belajar anak berkembang lebih optimal."
        )

    # =========================================
    # VISUAL + AUDITORY
    # =========================================

    elif (
        visual >= 35
        and
        auditory >= 25
    ):

        student.append(
            "Gunakan video pembelajaran, mind mapping, dan diskusi aktif untuk memperkuat pemahaman materi."
        )

        teacher.append(
            "Kombinasikan media visual dengan penjelasan verbal dan diskusi kelas."
        )

        parent.append(
            "Dukung anak belajar menggunakan video edukasi dan komunikasi aktif."
        )

    # =========================================
    # VISUAL + KINESTHETIC
    # =========================================

    elif (
        visual >= 35
        and
        kinesthetic >= 25
    ):

        student.append(
            "Gunakan media visual yang dipadukan dengan praktik langsung atau simulasi."
        )

        teacher.append(
            "Gunakan demonstrasi, eksperimen, dan project-based learning."
        )

        parent.append(
            "Berikan aktivitas belajar berbasis praktik dan visual di rumah."
        )

    # =========================================
    # AUDITORY + KINESTHETIC
    # =========================================

    elif (
        auditory >= 35
        and
        kinesthetic >= 25
    ):

        student.append(
            "Belajar melalui diskusi aktif, praktik langsung, dan simulasi kelompok."
        )

        teacher.append(
            "Gunakan pembelajaran interaktif berbasis aktivitas dan diskusi."
        )

        parent.append(
            "Ajak anak belajar sambil melakukan aktivitas sederhana dan komunikasi aktif."
        )

    # =========================================
    # HIGH VISUAL
    # =========================================

    if visual >= 60:

        student.append(
            "Kemampuan visual Anda sangat kuat. Gunakan diagram, warna, dan video untuk memaksimalkan pemahaman."
        )

    # =========================================
    # HIGH AUDITORY
    # =========================================

    if auditory >= 60:

        student.append(
            "Kemampuan auditori Anda sangat dominan. Diskusi, presentasi, dan penjelasan verbal akan sangat membantu proses belajar."
        )

    # =========================================
    # HIGH KINESTHETIC
    # =========================================

    if kinesthetic >= 60:

        student.append(
            "Kemampuan kinestetik Anda sangat dominan. Praktik langsung dan aktivitas fisik akan meningkatkan fokus belajar."
        )

    return {

        "student": student,

        "teacher": teacher,

        "parent": parent

    }