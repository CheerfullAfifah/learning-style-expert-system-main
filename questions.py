import random

questions = [

{
        "id": "q1",
        "question": "Ketika guru menjelaskan materi baru, hal yang paling membantumu memahami pelajaran adalah...",
        "options": [
            {"text": "melihat gambar, diagram, atau video", "type": "visual", "fact": "suka_visualisasi"},
            {"text": "mendengarkan penjelasan guru", "type": "auditory", "fact": "suka_penjelasan_lisan"},
            {"text": "mencoba langsung melalui praktik", "type": "kinesthetic", "fact": "suka_praktik"}
        ]
    },

    {
        "id": "q2",
        "question": "Saat belajar di rumah, kamu biasanya lebih nyaman dengan cara...",
        "options": [
            {"text": "membuat catatan berwarna atau mind map", "type": "visual", "fact": "suka_mindmap"},
            {"text": "mengulang materi dengan suara", "type": "auditory", "fact": "belajar_dengan_suara"},
            {"text": "belajar sambil bergerak", "type": "kinesthetic", "fact": "belajar_sambil_bergerak"}
        ]
    },

    {
        "id": "q3",
        "question": "Ketika menghafal pelajaran, kamu lebih mudah mengingat...",
        "options": [
            {"text": "bentuk tulisan, warna, atau gambar", "type": "visual", "fact": "mengingat_visual"},
            {"text": "suara atau penjelasan yang didengar", "type": "auditory", "fact": "mengingat_audio"},
            {"text": "hal yang pernah dipraktikkan", "type": "kinesthetic", "fact": "mengingat_pengalaman"}
        ]
    },

    {
        "id": "q4",
        "question": "Saat guru memberikan tugas kelompok, kamu lebih tertarik untuk...",
        "options": [
            {"text": "membuat desain atau slide presentasi", "type": "visual", "fact": "suka_desain"},
            {"text": "menjelaskan materi kepada kelompok", "type": "auditory", "fact": "suka_berbicara"},
            {"text": "menyiapkan demonstrasi atau praktik", "type": "kinesthetic", "fact": "suka_demonstrasi"}
        ]
    },

    {
        "id": "q5",
        "question": "Saat mempelajari hal baru, kamu biasanya lebih suka...",
        "options": [
            {"text": "melihat contoh visual terlebih dahulu", "type": "visual", "fact": "butuh_contoh_visual"},
            {"text": "mendengar penjelasan terlebih dahulu", "type": "auditory", "fact": "butuh_penjelasan_lisan"},
            {"text": "langsung mencoba sendiri", "type": "kinesthetic", "fact": "langsung_mencoba"}
        ]
    },

    {
        "id": "q6",
        "question": "Ketika belajar di kelas, kamu paling fokus jika...",
        "options": [
            {"text": "guru menggunakan gambar atau video", "type": "visual", "fact": "fokus_dengan_visual"},
            {"text": "guru menjelaskan dengan menarik", "type": "auditory", "fact": "fokus_dengan_audio"},
            {"text": "ada aktivitas praktik", "type": "kinesthetic", "fact": "fokus_dengan_praktik"}
        ]
    },

    {
        "id": "q7",
        "question": "Saat membaca buku pelajaran, kamu lebih suka jika...",
        "options": [
            {"text": "banyak gambar dan warna menarik", "type": "visual", "fact": "suka_buku_visual"},
            {"text": "dibaca sambil bersuara pelan", "type": "auditory", "fact": "membaca_bersuara"},
            {"text": "disertai aktivitas praktik", "type": "kinesthetic", "fact": "butuh_aktivitas"}
        ]
    },

    {
        "id": "q8",
        "question": "Ketika suasana kelas ramai, kamu biasanya tetap bisa belajar jika...",
        "options": [
            {"text": "masih bisa melihat materi dengan jelas", "type": "visual", "fact": "mengandalkan_penglihatan"},
            {"text": "masih bisa mendengar penjelasan", "type": "auditory", "fact": "mengandalkan_pendengaran"},
            {"text": "tetap melakukan aktivitas belajar", "type": "kinesthetic", "fact": "mengandalkan_aktivitas"}
        ]
    },

    {
        "id": "q9",
        "question": "Saat menggunakan HP untuk belajar, kamu paling sering...",
        "options": [
            {"text": "menonton video pembelajaran", "type": "visual", "fact": "suka_video"},
            {"text": "mendengarkan podcast atau audio", "type": "auditory", "fact": "suka_podcast"},
            {"text": "mengikuti simulasi interaktif", "type": "kinesthetic", "fact": "suka_simulasi"}
        ]
    },

    {
        "id": "q10",
        "question": "Jika guru memberi instruksi, kamu lebih cepat memahami ketika...",
        "options": [
            {"text": "instruksi ditulis atau diperlihatkan", "type": "visual", "fact": "memahami_visual"},
            {"text": "instruksi dijelaskan langsung", "type": "auditory", "fact": "memahami_lisan"},
            {"text": "instruksi dicontohkan langsung", "type": "kinesthetic", "fact": "memahami_praktik"}
        ]
    },
    {
        "id": "q11",
        "question": "Saat belajar bersama teman, kamu lebih nyaman jika...",
        "options": [
            {"text": "ada catatan atau gambar yang bisa dilihat bersama", "type": "visual", "fact": "belajar_dengan_gambar"},
            {"text": "belajar sambil berdiskusi", "type": "auditory", "fact": "belajar_diskusi"},
            {"text": "belajar sambil praktik", "type": "kinesthetic", "fact": "belajar_praktik"}
        ]
    },

    {
        "id": "q12",
        "question": "Hal yang paling mudah kamu ingat setelah belajar biasanya adalah...",
        "options": [
            {"text": "apa yang kamu lihat", "type": "visual", "fact": "ingat_apa_yang_dilihat"},
            {"text": "apa yang kamu dengar", "type": "auditory", "fact": "ingat_apa_yang_didengar"},
            {"text": "apa yang kamu lakukan", "type": "kinesthetic", "fact": "ingat_apa_yang_dilakukan"}
        ]
    },

    {
        "id": "q13",
        "question": "Ketika guru menjelaskan terlalu lama, kamu biasanya...",
        "options": [
            {"text": "mulai mencoret-coret catatan", "type": "visual", "fact": "mengekspresikan_visual"},
            {"text": "masih mendengarkan penjelasan", "type": "auditory", "fact": "tetap_mendengar"},
            {"text": "mulai ingin bergerak", "type": "kinesthetic", "fact": "ingin_bergerak"}
        ]
    },

    {
        "id": "q14",
        "question": "Saat diminta menjelaskan sesuatu kepada teman, kamu lebih sering...",
        "options": [
            {"text": "menggunakan gambar atau tulisan", "type": "visual", "fact": "menjelaskan_dengan_visual"},
            {"text": "menjelaskan dengan berbicara", "type": "auditory", "fact": "menjelaskan_lisan"},
            {"text": "mencontohkan secara langsung", "type": "kinesthetic", "fact": "menjelaskan_praktik"}
        ]
    },

    {
        "id": "q15",
        "question": "Ketika melihat informasi baru, perhatianmu biasanya tertuju pada...",
        "options": [
            {"text": "warna, bentuk, atau tampilan visual", "type": "visual", "fact": "tertarik_visual"},
            {"text": "cara penyampaian penjelasan", "type": "auditory", "fact": "tertarik_audio"},
            {"text": "aktivitas yang bisa dilakukan", "type": "kinesthetic", "fact": "tertarik_aktivitas"}
        ]
    },

    {
        "id": "q16",
        "question": "Saat sedang santai, aktivitas yang paling kamu sukai adalah...",
        "options": [
            {"text": "menonton video atau melihat gambar", "type": "visual", "fact": "suka_gambar"},
            {"text": "mendengarkan musik atau ngobrol", "type": "auditory", "fact": "suka_musik"},
            {"text": "melakukan aktivitas fisik", "type": "kinesthetic", "fact": "suka_aktivitas_fisik"}
        ]
    },

    {
        "id": "q17",
        "question": "Jika ada alat peraga di kelas, kamu biasanya lebih suka...",
        "options": [
            {"text": "memperhatikan bentuk dan tampilannya", "type": "visual", "fact": "memperhatikan_bentuk"},
            {"text": "mendengarkan penjelasannya", "type": "auditory", "fact": "mendengar_penjelasan"},
            {"text": "mencobanya secara langsung", "type": "kinesthetic", "fact": "mencoba_langsung"}
        ]
    },

    {
        "id": "q18",
        "question": "Saat mengerjakan tugas sulit, kamu biasanya...",
        "options": [
            {"text": "mencari contoh visual", "type": "visual", "fact": "mencari_visual"},
            {"text": "bertanya atau berdiskusi", "type": "auditory", "fact": "bertanya_diskusi"},
            {"text": "mencoba sendiri berkali-kali", "type": "kinesthetic", "fact": "trial_and_error"}
        ]
    },

    {
        "id": "q19",
        "question": "Saat mengikuti pembelajaran online, kamu lebih nyaman jika...",
        "options": [
            {"text": "materinya penuh visual dan animasi", "type": "visual", "fact": "suka_animasi"},
            {"text": "penjelasan suara terdengar jelas", "type": "auditory", "fact": "suka_audio_jelas"},
            {"text": "ada tugas praktik atau interaksi", "type": "kinesthetic", "fact": "suka_interaksi"}
        ]
    },

    {
        "id": "q20",
        "question": "Saat bermain game edukasi, bagian yang paling kamu sukai adalah...",
        "options": [
            {"text": "tampilan visual game", "type": "visual", "fact": "suka_tampilan_game"},
            {"text": "suara dan dialog game", "type": "auditory", "fact": "suka_suara_game"},
            {"text": "gerakan dan aksi dalam game", "type": "kinesthetic", "fact": "suka_aksi_game"}
        ]
    },
    {
        "id": "q21",
        "question": "Kegiatan sekolah yang paling membuatmu semangat biasanya adalah...",
        "options": [
            {"text": "yang memiliki tampilan menarik", "type": "visual", "fact": "suka_tampilan_menarik"},
            {"text": "yang banyak diskusi dan komunikasi", "type": "auditory", "fact": "suka_komunikasi"},
            {"text": "yang melibatkan praktik langsung", "type": "kinesthetic", "fact": "suka_praktik_langsung"}
        ]
    },

    {
        "id": "q22",
        "question": "Saat mempelajari materi baru, kamu lebih mudah memahami jika...",
        "options": [
            {"text": "ada diagram atau ilustrasi", "type": "visual", "fact": "memahami_dengan_diagram"},
            {"text": "ada penjelasan verbal yang jelas", "type": "auditory", "fact": "memahami_dengan_penjelasan"},
            {"text": "ada percobaan atau simulasi", "type": "kinesthetic", "fact": "memahami_dengan_simulasi"}
        ]
    },

    {
        "id": "q23",
        "question": "Ketika belajar untuk ujian, kamu lebih sering...",
        "options": [
            {"text": "membaca ulang catatan atau rangkuman", "type": "visual", "fact": "membaca_rangkuman"},
            {"text": "mengulang materi dengan suara", "type": "auditory", "fact": "mengulang_dengan_suara"},
            {"text": "belajar sambil bergerak", "type": "kinesthetic", "fact": "belajar_sambil_bergerak_lagi"}
        ]
    },

    {
        "id": "q24",
        "question": "Jika diminta membuat suatu karya, kamu lebih suka...",
        "options": [
            {"text": "mendesain tampilan yang menarik", "type": "visual", "fact": "suka_mendesain"},
            {"text": "menjelaskan ide kepada orang lain", "type": "auditory", "fact": "suka_menjelaskan_ide"},
            {"text": "membuat model atau praktik langsung", "type": "kinesthetic", "fact": "suka_membuat_model"}
        ]
    },

    {
        "id": "q25",
        "question": "Saat belajar kelompok, kamu paling sering...",
        "options": [
            {"text": "menulis atau membuat rangkuman visual", "type": "visual", "fact": "membuat_rangkuman_visual"},
            {"text": "berdiskusi dan bertukar pendapat", "type": "auditory", "fact": "bertukar_pendapat"},
            {"text": "menyiapkan aktivitas praktik", "type": "kinesthetic", "fact": "menyiapkan_praktik"}
        ]
    },

    {
        "id": "q26",
        "question": "Saat guru memberikan contoh materi, kamu lebih mudah memahami jika...",
        "options": [
            {"text": "contohnya berupa gambar atau ilustrasi", "type": "visual", "fact": "contoh_gambar"},
            {"text": "contohnya dijelaskan secara lisan", "type": "auditory", "fact": "contoh_lisan"},
            {"text": "contohnya dipraktikkan langsung", "type": "kinesthetic", "fact": "contoh_praktik"}
        ]
    },

    {
        "id": "q27",
        "question": "Ketika belajar sesuatu yang baru, langkah pertama yang biasanya kamu lakukan adalah...",
        "options": [
            {"text": "melihat contoh atau tampilan visual", "type": "visual", "fact": "melihat_contoh"},
            {"text": "mendengarkan penjelasan terlebih dahulu", "type": "auditory", "fact": "mendengar_penjelasan_awal"},
            {"text": "langsung mencoba sendiri", "type": "kinesthetic", "fact": "mencoba_langsung_awal"}
        ]
    },

    {
        "id": "q28",
        "question": "Saat suasana kelas mulai membosankan, kamu biasanya...",
        "options": [
            {"text": "melihat-lihat catatan atau gambar", "type": "visual", "fact": "melihat_catatan"},
            {"text": "mengobrol dengan teman", "type": "auditory", "fact": "mengobrol"},
            {"text": "bergerak atau memainkan sesuatu", "type": "kinesthetic", "fact": "memainkan_sesuatu"}
        ]
    },

    {
        "id": "q29",
        "question": "Saat mengikuti presentasi di kelas, bagian yang paling membantumu memahami materi adalah...",
        "options": [
            {"text": "slide dan visual presentasi", "type": "visual", "fact": "memahami_slide"},
            {"text": "cara pembicara menjelaskan", "type": "auditory", "fact": "memahami_penjelasan_pembicara"},
            {"text": "demonstrasi atau simulasi langsung", "type": "kinesthetic", "fact": "memahami_demonstrasi"}
        ]
    },

    {
        "id": "q30",
        "question": "Menurutmu, cara belajar yang paling menyenangkan adalah...",
        "options": [
            {"text": "belajar dengan tampilan visual menarik", "type": "visual", "fact": "suka_visual_menarik"},
            {"text": "belajar sambil berdiskusi", "type": "auditory", "fact": "suka_diskusi"},
            {"text": "belajar sambil praktik langsung", "type": "kinesthetic", "fact": "suka_praktik_final"}
        ]
    },
]

for q in questions:
    random.shuffle(q["options"])