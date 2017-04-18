'''
Created on 16.04.2017

@author: MScharf
'''

class State(object):
    def __init__(self, name):
        self._name = name
        self._enter = ""
        self._exit=""
        self._do=""
        self._history=""
        self._event={}
    
    
    def getEnter(self):
        return self._enter;
    def setEnter(self, enter):
        self._enter = enter
    def getExit(self):
        return self._exit
    def setExit(self, _exit):
        self._exit = _exit;
    def getDo(self):
        return self._do
    def setDo(self, do):
        self._do = do
        pass
    
    def addEvent(self, event, effect):
        if type(effect) is not str:
            print("addEvent failed for "+ self._name + ": " + event + ":" + effect + " isn't a valid combination")
            return 
        if self._event.has_key(event):
            print("State " + self._name + " already contains trigger "+ event + ", will be overwritten!")
        self._event[event] = effect
        
    def __str__(self):
        result = self._name+"\n"
        if not self._enter:
            result += "\tno enter trigger\n"
        else:
            result += "\tenter="+self._enter+"\n"
        if not self._exit:
            result += "\tno exit trigger\n"
        else:
            result += "\exit="+self._exit+"\n"
        if not self._do:
            result += "\tno do trigger\n"
        else:
            result += "\do="+self._do+"\n"
            
        result += self._
    
    
    #property for enter event
    enterTrigger = property(getEnter, setEnter)
    exitTrigger = property(getExit, setExit)
    doTrigger = property(getDo, setDo)


if __name__ == '__main__':
    naso = State("Naso")
    naso.doTrigger = "HasenHirn"
    naso.enterTrigger = "MilchKatzenWampa"
    print naso.
    pass