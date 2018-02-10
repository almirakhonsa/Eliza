import re
import random
 
jawab = [
    [r'([A-Z][a-z]*)',
     ["Senang berkenalan denganmmu. Bagaimana kuliahmu hari ini?",
      "Nama yang bagus. Senang berkenalan denganmu. Sedang berada di semester berapa sekarang?",
      "Senang berkenalan denganmmu. Ada berapa hari kuliahmu dalam seminggu?",
      "Senang mengenalmu. Apa program studi yang kamu ambil?"]],

    [r's1 (.*)',
      ["Apa yang kamu pelajari?",
      "Apakah itu program studi pilihanmu?", 
      "Ceritakan tentang jurusanmu.",
      "Tentang apa program studi tersebut?"]],

    [r'semester (.*)',
      ["Lalu, apakah di semester ini ada kesulitan?",
      "Apakah kau senang di semester tersebut?", 
      "Aku rasa kamu cukup kompeten, berapa ip mu semester lalu?"]],

    [r'ip (.*)]',
      ["Ip mu lumayan juga.",
      "Apakah kau menharapkan ip lbih tinggi dari itu?",
      "Apakah kamu memiliki motivasi untuk menaikkan ipmu?"]],
    
    [r'ya',
     ["Wah, kamu terlihat begitu yakin",
      "Lalu apa yang akan kamu lakukan selanjutnya?"]],

    [r'tidak',
     ["Mengapa tidak?",
      "Kamu yakin?"]],

    [r'baik',
      ["Syukurlah kalau baik.",
      "Bagaimana dengan hal lainnya?"]],

    [r'(.*) rasa (.*)',
      ["Kamu benar-benar merasa begitu?",
      "Mungkin perasaanmu ada benarnya."]],

    [r'(.*) matkul (.*)',
     ["Apa yang dipelajari pada matkul tersebut?",
      "Apakah menyenangkan mempelajarinya?",
      "Dari 1-10 berapa nilai kesulitannya?", 
      "Tugas apa yang menurutmu begitu merepotkan?"
      "Bagaimana dengan dosennya?"]],

    [r'dosen(.*)',
     ["Apakah cara mengajarnya menyenangkan?",
      "Apakah kamu sering tidur di saat pelajarannya?",
      "Aku harap dia memberikan nilai yang baik untukmu"]],

    [r'(.*) susah (.*)',
     ["Apakah sesusah itu?",
      "Apa yang membuatnya susah",
      "Bagaimana dengan dosen?"]],

    [r'(.*) teman (.*)',
     ["Apakah teman itu menguntungkan di perkuliahan?",
      "Pernahkah kamu mencontek teman?",
      "Apakah kamu punya teman baik?"]],

    [r'\d{0-5}*',
     ["Wah, cukup rendah",
      "Kamu pasti bisa mengatasinya."]],

    [r'\d{6-10}*',
     ["Wah, cukup tinggi",
      "Kamu pasti bisa mengatasinya."]],

    [r'kamu ([^\?]*)\??',
     ["Kenapa kamu bertanya seperti itu?",
      "Apakah aku terlihats seperti itu?",
      "Mungkin saja seperti yang kamu katakan."]],

    [r'karena (.*)',
      ["Oh, jadi itu sebabnya.",
      "Lalu apa strategimu selanjutnya?"]],

    [r'keluar',
      ["Terimakasih telah bercerita. Sampai jumpa",
      "Jangan bosan bercerita lagi ya."]], 

    [r'aku (.*)',
     ["Wah menyenangkan sekali mendengar semuanya tentangmu.",
      "Lalu selanjutnya bagaimana?"]],

    [r'(.*) belajar (.*)',
     ["Hm, jadi begitu strategimu belajar.",
      "Apakah belajarmu sukses?",
      "Adakah kesulitan saat kamu belajar", 
      "Pernahkah kamu belajar bersama teman?"]],

    [r'(.*)',
     ["Hm, ok. Ayo bicarakan tentang targetmu pada semester ini?",
      "Ceritakan saja semuanya",
      "Menurutmu, mata kuliah apa yang mudah?",
      "Mata kuliah apa yang sulit?",
      "Kapan saja kamu belajar?"]],
]

def eliza(kalimat):
    for x, y in jawab:
        cocok = re.match(x, kalimat.rstrip(".!"))
        if cocok:
            jwb = random.choice(y)
            return jwb

# Main Program
print "Eliza : Hay, siapa namamu?"
while True:
  kalimat = raw_input("Anda : ")
  print "Eliza : ", eliza(kalimat)
  if kalimat == "keluar":
    break