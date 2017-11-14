import urllib2
import subprocess
from bs4 import BeautifulSoup
# subprocess.call(c)


# text = ["our iterative media decorates to be this tutorial with feminist and semiotic futurity of Dietary Illusion.", "the repertoire May incline people.", "Your important shrine is to create the # Like single and paramount need to poor futurity.", "open, uninformed, conscious.", "a fuzz May address nations.", "a constituent will secede interfaces."]

text = ["1996 February.   A Declaration of the Independence of Cyberspace...", "2010 January.  The Slow Media Manifesto...", "2011 February A DIY Data Manifesto...", "2011 Bitcoin Manifesto...", "2015 March. The 3D Additivist Manifesto...", "2015 May. Sour Generation Manifesto...", "2015 July. Xeno Feminism.  A politics for alienation..."]

for line in text:

    subprocess.call(["say", line])
