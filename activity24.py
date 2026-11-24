#hobby

SwordofDisasters = "The true power of the Sky attribute is that it is significantly louder and rumbles like a tsunami."
FireSword = "A sword shining bright with its fire surrounding it."
DominatingAura = "Anyone who experiences this must bow down to their knees."
VitalityoftheHeart = "Blood flows through his body more than the normal person."
IndestructableShield = "This a shield with wings, capable of defending anything."
Record = "The ability to memorise any text within seconds."
Swordmaster = "More skilled at sword art than the average knight."
BlackYong = "A traditional Korean dragon bursts out of his sword."
ControllingWyverns = "The ability to control Wyverns."

CHApp = "A young man with black hair, black eyes, and a lean, athletic build."
WSApp = "A man with an imposing appearance and an intimidating presence."
CaleApp = "A young nobleman with red hair, a handsome face, and a slender build."

CHBeh = "Quiet, respectful, and composed, but ruthless when protecting those he cares about."
WSBeh = "Arrogant, manipulative, ambitious, and cruel toward those he considers inferior."
CaleBeh = "Laid-back and calculating, often pretending to be lazy while secretly helping others."

CHPer = "Kind-hearted, loyal, hardworking, and determined."
WSPer = "Power-hungry, selfish, prideful, and obsessed with gaining strength."
CalePer = "Pragmatic, intelligent, caring, and self-sacrificing."

MAlCH = "Choi Han"
ONaCH = "Black Dragon Slayer"
IdenCH = "A person transported from Earth to another world."

MAlWS = "White Star"
ONaWS = "The White Star"
IdenWS = "The leader of the White Star organization."

MACale = "Cale Henituse"
ONCale = "Kim Rok Soo"
IdenCale = "Trash of the Count's Family."

WSAbnPow = [SwordofDisasters,FireSword,DominatingAura] #3
CaleAbnPow = [VitalityoftheHeart,IndestructableShield,Record] #3
CHAbnPow = [Swordmaster,BlackYong,ControllingWyverns] #3

CHDesc = [CHApp,CHBeh,CHPer] #3
WSDesc = [WSApp,WSPer,WSPer] #3
CaleDesc = [CaleApp,CalePer,CaleBeh] #3

CHKnoN = [MAlCH,ONaCH,IdenCH] #3
WSKnoN = [MAlWS,ONaWS,IdenWS] #3
CaleKnoN = [MACale,ONCale,IdenCale] #3

WhiteStar = [WSDesc,WSKnoN,WSAbnPow] #2
ChoiHan = [CHDesc,CHKnoN,CHAbnPow] #2
Cale = [CaleDesc,CaleKnoN,CaleAbnPow] #2
LCF = [Cale,WhiteStar,ChoiHan] #1

# Sara = "A high school student who finds herself trapped in a deadly game where participants must make difficult decisions to survive."
# Joe = "Sara's cheerful and supportive best friend who tries to keep everyone's spirits up."
# Sou = "A mysterious and manipulative participant who often hides his true intentions."

DescSara = "A high school student who finds herself trapped in a deadly survival game."
AliSara = "Sara Chidouin, Main Protagonist."
AgeSara = "17 years old."

DescJoe = "A cheerful high school student and Sara's best friend."
AliJoe = "Joe Tazuna."
AgeJoe = "17 years old."

DescSou = "A mysterious participant in the deadly survival game."
AliSou = "Sou Hiyori, Shin Tsukimi."
AgeSou = "Varies depending on the identity being discussed."

bffSara = "Joe Tazuna."
FamSara = "Reko and Alice are fellow participants, not family members."
AllSara = "Participants who cooperate with Sara throughout the death game."

bffJoe = "Sara Chidouin."
FamJoe = "Has a family outside the death game."
AllJoe = "Sara and the other participants."

ConSou = "Has connections to the other participants."
RivSou = "Sara Chidouin."
AllSou = "His alliances are often uncertain."

PerSara = "Intelligent, observant, and determined."
StrSara = "Leadership, problem-solving, and decision-making."
WeakSara = "Can be emotionally affected by difficult decisions."

PerJoe = "Friendly, humorous, and optimistic."
StrJoe = "Loyalty, kindness, and emotional support."
WeakJoe = "Can be overly trusting and vulnerable."

PerSou = "Secretive, manipulative, and intelligent."
StrSou = "Strategic thinking and deception."
WeakSou = "Distrustful and emotionally conflicted."

PerInSara = [DescSara, AliSara, AgeSara] #3
PerInJoe = [DescJoe, AliJoe, AgeJoe] #3
PerInSou = [DescSou, AliSou, AgeSou] #3

RelaSara = [bffSara, FamSara, AllSara] #3
RelaJoe = [bffJoe, FamJoe, AllJoe] #3
RelaSou = [ConSou, RivSou, AllSou] #3

CharSara = [PerSara, StrSara, WeakSara] #3
CharJoe = [PerJoe, StrJoe, WeakJoe] #3
CharSou = [PerSou, StrSou, WeakSou] #3

Sara = [PerInSara, RelaSara, CharSara] #2
Joe = [PerInJoe, RelaSara, CharSara] #2
Sou = [PerInSou, RelaSou, CharSou] #2
YTTD = [Sara,Joe,Sou] #1

# Anastasya = ["Artifacts","Weapons","Teams"] #2
# Charlotte = ["Artifacts","Weapons","Teams"] #2
# Zibai = ["Artifacts","Weapons","Teams"] #2
# GENSHIN = [Anastasya,Charlotte,Zibai] #1
FavMedia = {"novel":LCF,"visualnovel":YTTD }#,"videogame":GENSHIN}

print(FavMedia["novel"][1][0][1])