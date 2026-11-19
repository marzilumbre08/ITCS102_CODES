#hobby
#novels

SwordofDisasters = "The true power of the Sky attribute is that it is significantly louder and rumbles like a tsunami."
FireSword = "A sword shining bright with its fire surrounding it."
DominatingAura = "Anyone who experiences this must bow down to their knees."
VitalityoftheHeart = "Blood flows through his body more than the normal person."
IndestructableShield = "This a shield with wings, capable of defending anything."
Record = "The ability to memorise any text within seconds."
Swordmaster = "More skilled at sword art than the average knight."
BlackYong = "A traditional Korean dragon bursts out of his sword."
ControllingWyverns = "The ability to control Wyverns"



WS = [SwordofDisasters,FireSword,DominatingAura]
Cale = [VitalityoftheHeart,IndestructableShield,Record]
ChoiHan = [Swordmaster,BlackYong,ControllingWyverns]
LCF = [Cale,WS,ChoiHan]
Novels = [LCF,ORV]


print(Novels["fav"][1][0])