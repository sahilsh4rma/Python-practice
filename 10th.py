song="tu tu hai wahi dil ne jise apna kaha Tu hai jahan main hoon wahan Ab to yeh jeena tere bin hai sazaa Ho mil jaayein is tarah do leharein jis tarah Ho mil jaayein is tarah do leharein jis tarah Phir hon na judaa haan yeh vaada raha Main aawaz hoon to tu hai geet mera Main aawaz hoon to tu hai geet mera Jahan se nirala manmeet mera Mil jaayein is tarah do leharein jis tarah Ho mil jaayein is tarah do leharein jis tarah Phir hon na judaa haan yeh vaada raha Tu tu hai wahi dil ne jise apna kaha Tu hai jahan main hoon wahan Ab to yeh jeena tere bin hai sazaa Kisi mod pe bhi na yeh sath toote Mere hath se tera daaman na chhoote Kabhi khwaab mein bhi tu mujhse na roothe Mere pyar ki koyi khushiyaan na loote Mil jaayein is tarah do leharein jis tarah Ho mil jaayein is tarah do leharein jis tarah Phir hon na judaa haan yeh vaada raha Tu tu hai wahi dil ne jise apna kaha Tu hai jahan main hoon wahan Ab to yeh jeena tere bin hai sazaa Tujhe main jahan ki nazar se chura loon Kahin dil ke kone main tujhko chhupa loon Kabhi zindagi mein pade mushkilein to Mujhe tu sambhaale tujhe main sambhaloon Ho mil jaayein is tarah do leharein jis tarah Ho mil jaayein is tarah do leharein jis  Phir hon na judaa haan yeh vaada raha Tu tu hai wahi dil ne jise apna kaha Tu hai jahan main hoon wahan Ab to yeh jeena tere bin hai sazaa Phir hon na judaa haan yeh vaada raha Yeh vaada raha"

song_list=song.split()
def lyricsOp(song_list):
    words=[]                    
    need_words=[]
    max_freq=0
    for i in song_list:
        if i not in words and song_list.count(i)>max_freq:
            words.append(i)
            max_freq=song_list.count(i)
    for j in words:
        if song_list.count(j)==max_freq:
            need_words.append(j)
    return (need_words,max_freq)
x=lyricsOp(song_list)
print(x)
