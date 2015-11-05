from mainHandler import *
from potentialCode import *


def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def convertFloat(x):
    """
    Converts string to float, if float is None, 0 is returned
    """
    if x and isFloat(x):
        return float(x)
    else:
        return 0.0
        
class result(mainHandler):
    """
    Class which handles result page
    """
    def get(self):
        #This portion takes the input values provided at home page
        sou = int(self.request.get('source')) # no of sources
        vor = int(self.request.get('vortex')) # no of vortices
        dou = int(self.request.get('doublet')) #no of doublet
        #Every entity is represented by a tuple, source is a list all these tuples
        sources = []
        #vortices store info for all vortices
        vortices = []
        #doublets store info for all doublets
        doublets = []
        
        for so in range(sou):
            s = str(so)
            x = convertFloat(self.request.get('source_x' + s))
            y = convertFloat(self.request.get('source_y' + s))
            m = convertFloat(self.request.get('source_m' + s))
            sources.append((x, y, m))

        for v in range(vor):
            s = str(v)
            x = convertFloat(self.request.get('vortex_x' + s))
            y = convertFloat(self.request.get('vortex_y' + s))
            m = convertFloat(self.request.get('vortex_m' + s))
            vortices.append((x, y, m))

        for d in range(dou):
            s = str(d)
            x = convertFloat(self.request.get('doublet_x' + s))
            y = convertFloat(self.request.get('doublet_y' + s))
            m = convertFloat(self.request.get('doublet_m' + s))
            doublets.append((x, y, m))

        u = float(self.request.get('u'))
        alpha = float(self.request.get('alpha'))
        #Generation of objects for each entity
        entities = [] #list for saving all objects
        #source generation
        
        for s in sources:
            entities.append(source(s[2], (s[0], s[1])))
        for v in vortices:
            entities.append(vortex(v[2], (v[0], v[1])))
        for d in doublets:
            entities.append(doublet(d[2], (d[0], d[1])))

        entities.append(uniform(u, alpha))
        
        image_si = plotsifi(entities)
        image_quiver = plotquiver(entities)
        caption = getCaption(entities)
        user = users.get_current_user()
        if user:
            username = user.nickname()
            loginLink = users.create_login_url(self.request.uri)
            logoutLink = users.create_logout_url(self.request.uri)
        else:
            username = None
            loginLink = users.create_login_url(self.request.uri)
            logoutLink = "/"
        self.renderPage("result.html", plot_si = image_si, plot_quiver = image_quiver, caption = caption, username = username, loginLink = loginLink, logoutLink = logoutLink)
