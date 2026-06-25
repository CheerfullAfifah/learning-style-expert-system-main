# =====================================
# RESULT CALCULATION
# =====================================

def calculate_result(

    questions,
    answers

):

    facts = []

    for q in questions:

        question_id = str(
            q["id"]
        )

        selected_answer = answers.get(
            question_id
        )

        if selected_answer:

            facts.append(
                selected_answer
            )

    return facts

# =====================================
# FORWARD CHAINING
# =====================================
RULES = {

    "visual": [

        "suka_visualisasi",
        "suka_mindmap",
        "mengingat_visual",
        "suka_desain",
        "butuh_contoh_visual",

        "fokus_dengan_visual",
        "suka_buku_visual",
        "mengandalkan_penglihatan",
        "suka_video",
        "memahami_visual",

        "belajar_dengan_gambar",
        "ingat_apa_yang_dilihat",
        "mengekspresikan_visual",
        "menjelaskan_dengan_visual",
        "tertarik_visual",

        "suka_gambar",
        "memperhatikan_bentuk",
        "mencari_visual",
        "suka_animasi",
        "suka_tampilan_game",

        "suka_tampilan_menarik",
        "memahami_dengan_diagram",
        "membaca_rangkuman",
        "suka_mendesain",
        "membuat_rangkuman_visual",

        "contoh_gambar",
        "melihat_contoh",
        "melihat_catatan",
        "memahami_slide",
        "suka_visual_menarik"
    ],

    "auditory": [

        "suka_penjelasan_lisan",
        "belajar_dengan_suara",
        "mengingat_audio",
        "suka_berbicara",
        "butuh_penjelasan_lisan",

        "fokus_dengan_audio",
        "membaca_bersuara",
        "mengandalkan_pendengaran",
        "suka_podcast",
        "memahami_lisan",

        "belajar_diskusi",
        "ingat_apa_yang_didengar",
        "tetap_mendengar",
        "menjelaskan_lisan",
        "tertarik_audio",

        "suka_musik",
        "mendengar_penjelasan",
        "bertanya_diskusi",
        "suka_audio_jelas",
        "suka_suara_game",

        "suka_komunikasi",
        "memahami_dengan_penjelasan",
        "mengulang_dengan_suara",
        "suka_menjelaskan_ide",
        "bertukar_pendapat",

        "contoh_lisan",
        "mendengar_penjelasan_awal",
        "mengobrol",
        "memahami_penjelasan_pembicara",
        "suka_diskusi"
    ],

    "kinesthetic": [

        "suka_praktik",
        "belajar_sambil_bergerak",
        "mengingat_pengalaman",
        "suka_demonstrasi",
        "langsung_mencoba",

        "fokus_dengan_praktik",
        "butuh_aktivitas",
        "mengandalkan_aktivitas",
        "suka_simulasi",
        "memahami_praktik",

        "belajar_praktik",
        "ingat_apa_yang_dilakukan",
        "ingin_bergerak",
        "menjelaskan_praktik",
        "tertarik_aktivitas",

        "suka_aktivitas_fisik",
        "mencoba_langsung",
        "trial_and_error",
        "suka_interaksi",
        "suka_aksi_game",

        "suka_praktik_langsung",
        "memahami_dengan_simulasi",
        "belajar_sambil_bergerak_lagi",
        "suka_membuat_model",
        "menyiapkan_praktik",

        "contoh_praktik",
        "mencoba_langsung_awal",
        "memainkan_sesuatu",
        "memahami_demonstrasi",
        "suka_praktik_final"
    ]
}

FORWARD_RULES = [

    {
        "id": "V1",
        "if": [
            "suka_visualisasi",
            "suka_mindmap"
        ],
        "then": "visual_basic_1"
    },

    {
        "id": "V2",
        "if": [
            "mengingat_visual",
            "suka_desain"
        ],
        "then": "visual_basic_2"
    },

    {
        "id": "V3",
        "if": [
            "visual_basic_1",
            "visual_basic_2"
        ],
        "then": "visual"
    },

    {
        "id": "A1",
        "if": [
            "suka_penjelasan_lisan",
            "belajar_dengan_suara"
        ],
        "then": "auditory_basic_1"
    },

    {
        "id": "A2",
        "if": [
            "mengingat_audio",
            "suka_berbicara"
        ],
        "then": "auditory_basic_2"
    },

    {
        "id": "A3",
        "if": [
            "auditory_basic_1",
            "auditory_basic_2"
        ],
        "then": "auditory"
    },

    {
        "id": "K1",
        "if": [
            "suka_praktik",
            "belajar_sambil_bergerak"
        ],
        "then": "kinesthetic_basic_1"
    },

    {
        "id": "K2",
        "if": [
            "mengingat_pengalaman",
            "langsung_mencoba"
        ],
        "then": "kinesthetic_basic_2"
    },

    {
        "id": "K3",
        "if": [
            "kinesthetic_basic_1",
            "kinesthetic_basic_2"
        ],
        "then": "kinesthetic"
    }

]


