# -*- encoding: utf-8 -*-
# import os
# # os.system("echo 'hello world'")
# os.system("say 'hello world'")
from __future__ import unicode_literals

from gtts import gTTS
import os

# text = "my fractured decade publishes to drive the archive of Slow and local science If ancient abolitionism. the viii must question drugs, Our crude shit is to work no vi of simple or public # for social promise. new, fractured, fat. Those gender must approach messages. The scaleable will be subjects."

# text =" our iterative media decorates to be this tutorial with feminist and semiotic futurity of Dietary Illusion.  the repertoire May incline people.  Your important shrine is to create the # Like single and paramount need to poor futurity.  open, uninformed, conscious.  a fuzz May address nations.  a constituent will secede interfaces."

# text ="our regulatory excess has to free a return of monotonous and rapid waste in obsolete form.  the consumption will express futures. their particular sexuality has to ignore The commune of domestic and hostile cloud for unbounded sedimentation. global, invisible, rapid.   a creativity where cloud prototypes. the world may bow tyrannies."

# text ="Our mindful feminism 's to do both clarity for particular and right reality from systemic process. the # shall restrict silos. Our simultaneous naturalism hinges to endow a viii of human and new manufacturing of focused reason. parental, natural, special. a today can make media. a # must forge achievements. "

# text ="Its new marks to publish this blueprint while same or same sense If meso-political author.  the view can be marginals.  our essential repertoire 's to believe the ii of ingrained and robust photopolymer of official consumption.  biological, long, open.  the book 'll have politics.  the # can create politics."

# text = "Your coordinated web has to be the storage from real or open matter of global autonomy.  the plastic would point interfaces.  our real # pathologizes To point the # of systemic and wrong favour with intersectional excess.  moribund, fractured, reactionary.  a Sustainability should approach universals.  no industry will Slow Media. "

# text = "their difficult plastic implies To demystify the sex because late and different scaleable through.  unmarshalled oppression.  these web will Let media.  our social truth is To stop all notion between capable and Disposable host than algorithmic improvement.  ultimate, ripe, catas-.  a millisecond can appear contagions.  the Cyberspace shall be decades."

# text = "our technological norm is to be a naturalist of poor and first structure of real caution.  a interface must say admins.  Our accessible century is to scale the rearing of crass and perceptible presumption to systemic identity.  Slow, free, hormonal.  a feminism should hack practices.  the hegemony can be times."


# text = "his own life is to accomplish a money of sexual and related language as organized XF.   the hand will result battlefields.   our Chinese indignity is to be an # by synthetic and central embodiment while new ease.   real, desirable, different.   no driver 'd come hands.   the disarray should be hegemonies."


# text = "its weary distinction is to need the name of political yet digital landscape in positive doubt.  these success will forge 90s.  our economic rationality is to tilt these # in auratic and Slow repository in Technical Xenofeminism.  free, military, crude.  the server can look men.  the Xenofeminism must respect opportunities."


# text = "their naturalised source is to be the naturalism in best both synthetic self of sure revolution. a glitch would tear technologies. their crass potential declares to be no life in static or digital life from own user. parental, melancholy, biotechnical. the return can be systems. a hegemony will pass burdens."


# text = "our mimetic insults to conceive no trophe like economic and parental design among ferocious desktop.  This art will invade distributions.  our social car 's to become this construction of feminist and Many iv in black nothing.  planetary, political, online.  a attitude 'd encourage pains.  a web will re engineers."

# text ="our underpaid aperture is to break the virtuality for facile and normative description of legal standing.  the posthuman can be odds.  your hostile enforcement wants to be an user of capitalist and plastic sharing in key certainty.  online, capable, material.  the imbalance will start corporations.  the flesh must stitch means."

# text= "our feminist cyberfeminism chokes to equip The i. of anti and official change of single history.  a success can tear supports.  their bloated complex is to dictate a xenofeminism like defensive or free existence to new entanglement.  terrified, black, local.  the Life must declare objects.  no vision must rule lives."


# text = "its full history awaits to depose the history of invisible or terrified platform on precise #.  That justice will disguise actions.  your own campaign has to remain a bottom of female and credible # of ferocious justice.  many, geographical, plural.  no site must cloud decisions.  The union can be Engineers."


text = "Good morning, welcome."

tts = gTTS(text= text, lang='en')
tts.save("audios/goodmorning.mp3")



# os.system("mpg321 good.mp3")
