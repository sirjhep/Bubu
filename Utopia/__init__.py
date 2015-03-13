### Utopia ###

import time, requests, os
from pyquery import PyQuery
from datetime import datetime

class Utopia(object):
  def __init__(self, username, password):
    """Utopia Object: Instance for all Utopia Game operation"""
    
    self.user = username
    self.pwd = password
    self.csrftoken = False
    self.last_url = False
    
    self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
      "Host": "utopia-game.com",
      "Connection": "keep-alive",
      "Accept-Language": "en-US,en;q=0.5",
      "Accept-Encoding": "gzip, deflate",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "DNT": 1}
  
    self.page = {
      "login": "http://utopia-game.com/shared/login/",
      "logout": "http://utopia-game.com/shared//logout/?next=/",
      "Home": "http://utopia-game.com/shared/",
      "Lobby": "http://utopia-game.com/shared/lobby/",
      "Chooser": "http://utopia-game.com/wol/chooser/",
      "Throne": "http://utopia-game.com/wol/game/throne",
      "State": "http://utopia-game.com/wol/game/council_state",
      "Kingdom": "http://utopia-game.com/wol/game/kingdom_details",
      "Prov News": "http://utopia-game.com/wol/game/province_news",
      "Kd News": "http://utopia-game.com/wol/game/kingdom_news",
      "Explore": "http://utopia-game.com/wol/game/explore",
      "Growth": "http://utopia-game.com/wol/game/build",
      "Raze": "http://utopia-game.com/wol/game/raze",
      "Survey": "http://utopia-game.com/wol/game/council_internal",
      "Science": "http://utopia-game.com/wol/game/science",
      "SoS": "http://utopia-game.com/wol/game/council_learn",
      "Military": "http://utopia-game.com/wol/game/train_army",
      "SoM": "http://utopia-game.com/wol/game/council_military",
      "Wizards": "http://utopia-game.com/wol/game/wizards",
      "Mystics": "http://utopia-game.com/wol/game/enchantment",
      "Aura": "http://utopia-game.com/wol/game/council_spells",
      "Sorcery": "http://utopia-game.com/wol/game/sorcery",
      "Thievery": "http://utopia-game.com/wol/game/thievery",
      "War Room": "http://utopia-game.com/wol/game/send_armies",
      "Aid": "http://utopia-game.com/wol/game/aid",
      "Inbox": "http://utopia-game.com/wol/mail/inbox/",
      "Outbox": "http://utopia-game.com/wol/mail/outbox/",
      "Compose": "http://utopia-game.com/wol/mail/compose/",
      "Forums": "http://utopia-game.com/wol/kingdom_forum/topics/",
      "History": "http://utopia-game.com/wol/game/council_history",
      "Vote": "http://utopia-game.com/wol/game/vote/",
      "War": "http://utopia-game.com/wol/game/war/",
      "Nap": "http://utopia-game.com/wol/game/nap/",
      "Conflict": "http://utopia-game.com/wol/game/conflict/"
    }
    
    self.fox = requests.Session()

    self.log("Instance for "+self.user+" created")


  ########### METHODS ....

  ## Request Shorthands ##
  
  def get_head(self, page, allow_redirects=True):
    """ Sends a header request to page (Page must be within Utopia)"""
    try:
      return self.fox.head(self.page[page], headers = self.headers, allow_redirects=False)
    except requests.exceptions.ConnectionError:
      self.log( "Failed to get the header of "+page+" due to Network Problem." )
    except requests.exceptions.HTTPError:
      self.log( "Failed to get the header of "+page+" due to invalid HTTP response." )
    except requests.exceptions.Timeout:
      self.log( "Failed to get the header of "+page+" due to Time out." )
    except requests.exceptions.URLRequired:
      self.log( "Failed to get the header of "+page+" due to invalid url." )
    except:
      self.log( "Failed to get the header of "+page+" due to unknown errors" )
  
  def get(self, page, data=None):
    """Returns a Response object to GET request"""
    if self.last_url:
      self.headers["Referrer"] = self.last_url
    try:
      r = self.fox.get(self.page[page], headers = self.headers, data=data)
      self.last_url = r.url
      return r
    except requests.exceptions.ConnectionError:
      self.log( "Failed to get "+page+" due to Network Problem." )
    except requests.exceptions.HTTPError:
      self.log( "Failed to get "+page+" due to invalid HTTP response." )
    except requests.exceptions.Timeout:
      self.log( "Failed to get "+page+" due to Time out." )
    except requests.exceptions.URLRequired:
      self.log( "Failed to get "+page+" due to invalid url." )
    except:
      self.log( "Failed to get "+page+" due to unknown errors" )
  
  def post(self, page, data):
    """Returns a Response object to POST request"""
    try:
      r = self.fox.post(self.page[page], data = data, headers = self.headers)
      self.last_url = r.url
      if r.status_code > 340:
        self.log(str(r.raise_for_status()))
      return r
    except requests.exceptions.ConnectionError:
      self.log( "Failed to post "+page+" due to Network Problem." )
    except requests.exceptions.HTTPError:
      self.log( "Failed to post "+page+" due to invalid HTTP response." )
    except requests.exceptions.Timeout:
      self.log( "Failed to post "+page+" due to Time out." )
    except requests.exceptions.URLRequired:
      self.log( "Failed to post "+page+" due to invalid url." )
    except:
      self.log( "Failed to post "+page+" due to unknown errors" )

  ## Misc Function ##

  def numerize(self, string):
    if type(string) != type(str):
      return 0
    numonly = "".join([x for x in string if x.isdigit()])
    if numonly == "":
      return 0
    else:
      return int(numonly)

  def log(self, message):
    try:
      try:
        l = open("logs/"+self.user+".txt", "a")
      except IOError:
        os.makedirs("logs")
        l = open("logs/"+self.user+".txt", "a")
      l.write(str(datetime.now()) + ">>> " + message + "\n")
      l.close()
    except:
      print "There was something wrong writing the log."

  ## Utopia Interfaces ##
  
  def is_login(self):
    r = self.get_head("Throne")
    return r.status_code == 200

  def login(self):
    home = self.get("Home")
    if home is not None:
      self.csrftoken = home.cookies.get("csrftoken")
      data = {"username": self.user,
          "password": self.pwd,
          "csrfmiddlewaretoken": self.csrftoken}
      r = self.post("login", data)
      self.last_url = self.page["Throne"]
      if r.status_code == 200 and r.url == self.page["Lobby"]:
        self.log("Successfully Log-in as " + self.user)
        return True
      if r.status_code == 200 and r.url == self.page["login"]:
        self.log("Login Failed: Wrong Username or Password")
        return False
      else:
        print str(r.raise_for_status())
        return None
    else:
      self.log( "Failed to Log-In as " + self.user + ". Please check your internet connection." )
      return

  def logout(self):
    if self.is_login():
      self.get("logout")
      if not self.is_login():
        self.log("Log-Out")
        return True
      else:
        self.log("Failed to Log-Out")
        return False
      
  def pqfy(self, responseObj):
    return PyQuery(responseObj.text)

  def update_sot(self):
    if not self.is_login():
      self.login()
    throne = self.get("Throne")
    if throne is not None:
      T = self.pqfy(throne)
      h2n = T(".game-content > div:nth-child(1) > h2:nth-child(3)")
      h2 = h2n.text()
      box = T(".two-column-stats > tbody:nth-child(1)")("td")
      self.sot = {
          "uto date": h2[h2.find(") ")+2:],
          "ruler": "Ruler Name Here",
          "prov": h2[16:h2.find(" (")],
          "KD": h2n("a").text(),
          "pers": "Personality Here",
          "race": box[0].text,
          "land": self.numerize(box[4].text),
          "gold": self.numerize(box[10].text),
          "NW": self.numerize(box[18].text),
          "food": self.numerize(box[12].text),
          "runes": self.numerize(box[14].text),
          "peasants": self.numerize(box[6].text),
          "TB": self.numerize(box[16].text),
          "sols": self.numerize(box[1].text),
          "off spec": self.numerize(box[3].text),
          "def spec": self.numerize(box[5].text),
          "elites": self.numerize(box[7].text),
          "horses": self.numerize(box[13].text),
          "prisoners": self.numerize(box[15].text),
          "off points": self.numerize(box[17].text),
          "def points": self.numerize(box[19].text),
          "thieves": self.numerize(box[9].text.strip().split(" ")[0]),
          "stealth": self.numerize(box[9].text.strip().split(" ")[1]),
          "wizards": self.numerize(box[11].text.strip().split(" ")[0]),
          "mana": self.numerize(box[11].text.strip().split(" ")[1])
      }
      print "Successfully Updated SoT of "+self.sot['prov']
    
  def train(self,ospec=0,dspec=0,elites=0,thieves=0,rate=False,target=False,wage=False,accel=False):
    """Set Military Options:  Rate: NONE, RESERVIST, NORMAL, AGGRESSIVE, EMERGENCY
      target - Draft Limit: must be a number
      wage - The Wage rate: must be a number
      for troops, 0-1
    """
    if not self.is_login():
      self.login()
    milreq = self.get("Military")
    print len(milreq.history)
    if milreq is not None:
      mil = self.pqfy(milreq)
      td = mil(".game-content > form")("td")
      data = {
          'csrfmiddlewaretoken': self.csrftoken,
          'draft_rate': rate if rate else mil('#id_draft_rate option[selected]').val(),
          'draft_target': target if target else mil("#id_draft_target").val(),
          'wage_rate': wage if wage else mil("#id_wage_rate").val(),
          'unit-quantity_0': int(ospec*self.numerize(td[6].text)),
          'unit-quantity_1': int(dspec*self.numerize(td[11].text)),
          'unit-quantity_2': int(elites*self.numerize(td[16].text)),
          'unit-quantity_3': int(thieves*self.numerize(td[21].text))
        }
      if accel:
        data['unit-accelerate'] = 'on'
      res = self.post('Military', data)
      if res is not None:
        res = self.pqfy(res)
        for r in res("div.message"):
          print r.text.strip()
        return
    self.log( "Failed to operate on Military Page" )
      


  def learn(self,rate=False,minimum=False,gc=0,be=0,pop=0,food=0,me=0,tpa=0,wpa=0):
    """Rate: NO_RESEARCH, MINIMAL, LIMITED, SUSTAINED, ACTIVE, FOCUSED, ACCELERATED, INTENSIVE, RUSHED, EXTREME
    """
    if not self.is_login():
      self.login()
    scireq = self.get("Science")
    if scireq is not None:
      sci = self.pqfy(scireq)
      maxbooks = self.numerize(sci(".two-column-stats > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4)").text())
      data = {
          'csrfmiddlewaretoken': self.csrftoken,
          'learn_rate': rate if rate else sci('#id_learn_rate option[selected]').val(),
          'learn_min_income': minimum if minimum else int(sci("#id_learn_min_income").val()),
          'quantity_0': int(gc*maxbooks),
          'quantity_1': int(be*maxbooks),
          'quantity_2': int(pop*maxbooks),
          'quantity_3': int(food*maxbooks),
          'quantity_4': int(me*maxbooks),
          'quantity_5': int(tpa*maxbooks),
          'quantity_6': int(wpa*maxbooks)
          }
      res = self.post('Science', data)
      if res is not None:
        res = self.pqfy(res)
        for r in res("div.message"):
          print r.text.strip()
    self.log( "Failed to learn. Check connectivity." )



  def spells(self):
    """returns a dict of active spells as key with the duration left as value."""
    if not self.is_login():
      self.login()
    aura = self.get("Aura")
    if aura is not None:
      aurapq = self.pqfy(aura)
      ths = aurapq('.game-content > table:nth-child(2) > tbody:nth-child(2)')('th')
      tds = aurapq('.game-content > table:nth-child(2) > tbody:nth-child(2)')('td')
      auras = {}
      for i in range(len(ths)):
        auras[ths[i].find("div").text.strip()]=self.numerize(tds[i*2].text.strip())
      print "Active Spells acquired."
      return auras
    else:
      self.log( "Failed to acquire active spells" )
      return False


  def cast(self, spell,keep_retry=True,days=0,counter=1):
    """Cast a spell, if X is defined, refresh spells with duration X,do not set counter
      Returns 100 if there is no need to cast it.
      Returns 1XX if successful after XX tries.
      Returns 200 fails on cast (if keep_retry is False)
      Returns 2XX Fails and not enough runes on next cast.
    """
    spells = self.spells()
    if counter is not 1 and spell in spells:
      if spells[spell] > days:
        print "No need to cast "+spell+" coz its still on"
        return 100
    spellU = spell.replace(" ", "_").upper()
    data = {'csrfmiddlewaretoken': self.csrftoken,'spell': spellU}
    res = self.post('Mystics', data)
    res = self.pqfy(res)
    
    for r in res("div.message"):
      self.log(r.text.strip())
      
    if len(res("div.good")) > 0:
      self.log( "Successfully cast after " + counter + " tries." )
      return 100 + counter
    elif keep_retry:
      runesNode = '.two-column-stats > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4)'
      if self.numerize(res(runesNode).text) < self.numerize(res("#id_spell option[value="+spellU+"]").text()):
        self.log( "Not enought runes to cast "+spell )
        return 200 + counter
      else:
        self.log( "Failed. Retrying." )
        counter = counter + 1
        return self.cast(self, spell, True, days, counter)
    else:
      self.log( "Failed to cast" )
      return 200
