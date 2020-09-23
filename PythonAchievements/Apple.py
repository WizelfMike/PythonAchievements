import math

#Vervang de 0-en met de juiste berekeningen

trees               = 333             #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil(111)  #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = 222             #hoeveel in de zon?

shadeOutputModifier = 80             #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146             #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = 116.8             #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = 32412             #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = 12964             #hoeveel appels geven alle schaduw bomen?
totalOutput         = 45377             #hoeveel appels zijn er in totaal?

owners              = 3             #met hoeveel mensen verdelen we de appels?

eatCount            = 1.9             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = 45375             #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = 15125             #hoeveel appels mag ik verkopen?

print(cut)