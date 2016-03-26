import time; 
from ctypes import *; 
from random import randint 

# *********************************** 
# Dzwieki 
# *********************************** 
winmm = windll.winmm  
   
def mciSend(s):  
   i=winmm.mciSendStringW(s,None,0,0)  
   if i<>0:  
      diagnostics.debug("Error %d in mciSendString %s" % ( i, s ))  
   
def mciPlayBlocking(mp3Name):  
   mciSend('Close All')  
#   mciSend("Open \"%s\" Type MPEGVideo Alias theMP3" % mp3Name)  
   mciSend("Open \"%s\" Type Waveaudio Alias theMP3" % mp3Name)  
   mciSend("Play theMP3 Wait")  
   mciSend("Close theMP3")  

def wait(ile):
    klok=time.time()
    while time.time() < (klok+ile):
        pass
        

def graj(nazwa): 
   mciPlayBlocking('L:\GlovePie2\Elite\%s.wav' % nazwa) 

def KeyPress(key):
    keyboard.setKeyDown(key)
    wait(0.07)
    keyboard.setKeyUp(key)    

def KeyRepeat(key,times):
    for num in range(1,times):
        KeyPress(key)
        wait(0.1)

class Ship: 
        gear = 1 
        lights = 0 
        fireGroup = "weapons" 
        scoop = 0 
        hardpoints = 0 
        
        def __init__(self):
            diagnostics.debug("KONSTRUKTOR STATKU")
        
        def dump(self):
            diagnostics.debug("==============================")  
            diagnostics.debug("gear %d" % self.gear)  
            diagnostics.debug("ligh %d" % self.lights)  
            diagnostics.debug("fire %s" % self.fireGroup)  
            diagnostics.debug("scoo %d" % self.scoop)  
            diagnostics.debug("hard %d" % self.hardpoints)  

        def toggleGear(self):
            if(self.gear==0):
                self.setGear(1)
            else:
                self.setGear(0)

        def setGear(self,state): 
                if(self.gear!=state): 
                        KeyPress( Key.I ) 
                        if(state==1): 
                                graj("Misc_ActivatingLandingGear") 
                        else: 
                                graj("Misc_DeactivatingLandingGear") 
                        self.gear=state 

                self.dump()
                 
        def toggleLights(self): 
                if(self.lights==0):
                        self.setLights(1) 
                else: 
                        self.setLights(0) 
                
        def setLights(self,state):                 
                if(self.lights!=state): 
                        KeyPress( Key.L ) 
                        if(state==1): 
                                graj("Misc_Illuminating") 
                        else: 
                                graj("Misc_Deluminating") 
                        self.lights=state 
                self.dump()

        def setFireGroup(self,state):                 
                if(self.fireGroup!=state): 
                        if(state=="weapons"): 
                                graj("KICS_Weapons") 
                                KeyPress( Key.B ) 
                        else: 
                                graj("Driving_ActivatingDataLinkScanner") 
                                KeyPress( Key.N ) 
                        self.fireGroup=state 
                self.dump()

        def toggleScoop(self): 
                if(self.scoop==0): 
                        self.setScoop(1) 
                else: 
                        self.setScoop(0) 
                
        def setScoop(self,state):                 
                if(self.scoop!=state): 
                        if(state==1): 
                                graj("Misc_ActivatingCargoScoop") 
                        else: 
                                graj("Misc_DeactivatingCargoScoop") 
                        self.scoop=state
                self.dump()                        

        def toggleHardpoints(self): 
                if(self.hardpoints==0): 
                        self.setHardpoints(1) 
                else: 
                        self.setHardpoints(0) 
                
        def setHardpoints(self,state):                 
                if(self.hardpoints!=state): 
                        KeyPress( Key.U ) 
                        if(state==1): 
                                graj("Weapons_DeployingHardpoints") 
                        else: 
                                graj("Weapons_RetractingHardpoints") 
                        self.hardpoints=state
                self.dump()
                
        def faster(self): 
                KeyPress( Key.W ) 
                graj("FlightThrottle_IncreasingVelocity") 

        def slower(self):
                KeyPress( Key.S ) 
                graj("FlightThrottle_DecreasingVelocity") 

        def astern100(self):
                KeyPress( Key.NumberPad1 ) 
                graj("FlightThrottle_DecreasingVelocity") 

        def astern75(self): 
                KeyPress( Key.NumberPad2 ) 
                graj("FlightThrottle_Negative75") 
                
        def astern50(self): 
                KeyPress( Key.NumberPad3 ) 
                graj("FlightThrottle_Negative50") 
                
        def astern25(self): 
                KeyPress( Key.NumberPad4 ) 
                graj("FlightThrottle_Negative25") 
                
        def stop(self): 
                KeyPress( Key.NumberPad5 ) 
                graj("FlightThrottle_Stopping") 

        def ahead25(self): 
                KeyPress( Key.NumberPad6 ) 
                graj("FlightThrottle_Throttle25") 
                
        def ahead50(self): 
                KeyPress( Key.NumberPad7 ) 
                graj("FlightThrottle_Throttle50") 
                
        def ahdead75(self): 
                KeyPress( Key.NumberPad8 ) 
                graj("FlightThrottle_Throttle75") 
        
        def ahead100(self): 
                KeyPress( Key.NumberPad9 ) 
                graj("FlightThrottle_MaximumVelocity") 
        
        def boost(self): 
                KeyPress( Key.Tab ) 
                graj("FlightMisc_EngagingBoost") 
                
        def supercruise(self): 
                KeyPress( Key.Comma ) 
                graj("FlightMisc_ActivatingSupercruise") 
                
        def hyperspace(self): 
                KeyPress( Key.Period ) 
                graj("FlightMisc_PreparingForHyperspaceTravel") 

        def jump(self): 
                KeyPress( Key.J ) 
                graj("FlightMisc_EngagingFrameShiftDrive") 
                
        def target(self): 
                KeyPress( Key.T ) 
                graj("Targeting_LockingTarget") 
                
        def targetNext(self): 
                KeyPress( Key.G ) 
                graj("Targeting_TargetingNext") 
                
        def targetPrevious(self): 
                KeyPress( Key.D5 ) 
                graj("Targeting_TargetingPrevious") 
                
        def targetHostile(self): 
                KeyPress( Key.H ) 
                graj("Targeting_TargetingHighestThreat") 
                
        def targetNextHostile(self): 
                KeyPress( Key.D8 ) 
                graj("Targeting_TargetingNextHostile") 
                
        def targetPreviousHostile(self): 
                KeyPress( Key.Seven ) 
                graj("Targeting_TargetingNextHostile") 
                
        def targetNextSystem(self): 
                KeyPress( Key.D0 ) 
                graj("Targeting_TargetingNextSystem") 
                
        def targetPreviousSystem(self): 
                KeyPress( Key.D9 ) 
                graj("Targeting_TargetingPreviousSystem") 
                
        def balancePower(self): 
                KeyPress( Key.DownArrow ) 
                graj("KICS_Balancing") 
                
        def stepEngines(self): 
                KeyPress( Key.UpArrow ) 
                graj("KICS_AdjustingPower") 
                
        def stepWeapons(self): 
                KeyPress( Key.RightArrow ) 
                graj("KICS_AdjustingPower") 
                
        def stepShields(self): 
                KeyPress( Key.LeftArrow ) 
                graj("KICS_AdjustingPower") 
                
        def fullEngines(self): 
                KeyRepeat( Key.UpArrow, 5 ) 
                graj("KICS_AdjustingPower") 
                
        def fullWeapons(self): 
                KeyRepeat( Key.RightArrow, 5 ) 
                graj("KICS_AdjustingPower") 
                
        def fullShields(self): 
                KeyRepeat( Key.LeftArrow, 5 ) 
                graj("KICS_AdjustingPower") 
                
        def zoomIn(self): 
                KeyPress( Key.PageUp ) 
                graj("Misc_IncreasingSensorRange") 
                
        def zoomOut(self): 
                KeyPress( Key.PageDown ) 
                graj("Misc_DecreasingSensorRange") 
                
        def maxRange(self): 
                KeyRepeat( Key.PageUp, 8 ) 
                graj("Misc_MaximisingSensorRange") 
                
        def minRange(self): 
                KeyRepeat( Key.PageDown, 8 ) 
                graj("Misc_MinimisingSensorRange") 
                
        def galaxyMap(self): 
                KeyPress( Key.M ) 
                graj("ModeSwitches_AccessingGalaxyMap") 
                
        def systemMap(self): 
                KeyPress( Key.O ) 
                graj("ModeSwitches_AccessingSystemMap") 


def youreWelcome(): 
        r = randint(1,4) 
        if r == 1:
                graj("KICS_YouAreMostWelcome") 
        elif r == 2: 
                graj("KICS_Anytime") 
        elif r == 3:
                graj("KICS_AnytimeCommander") 
        elif r == 4:
                graj("KICS_YouAreWelcome") 
        
def what(): 
        r = randint(1,4) 
        if r == 1:
                graj("KICS_YesCommanderQ") 
        elif r == 2:
                graj("KICS_YesQ") 
        elif r == 3:
                graj("KICS_WhatIsItCommander") 
        elif r == 4:
                graj("KICS_HmmmQ") 
                
def ayAy(): 
        r = randint(1,7) 
        if r == 1:
                graj("KICS_AsYouWish") 
        elif r == 2:
                graj("KICS_AyeAye") 
        elif r == 3:
                graj("KICS_AyeCommander") 
        elif r == 4:
                graj("KICS_Certainly") 
        elif r == 5:
                graj("KICS_CertainlyCommander") 
        elif r == 6:
                graj("KICS_Done") 
        elif r == 7:
                graj("KICS_DoneCommander") 


def reguly(): 
        if speech.said("computer"): 
                what() 
        elif speech.said("thank you"): 
                youreWelcome() 
        elif speech.said("hello"): 
                graj("KICS_HelloCommander") 
        elif speech.said("can you hear me"): 
                graj("KICS_LoudAndClear") 
        
        elif speech.said("faster") or speech.said("speed up"): 
                myShip.faster() 
        elif speech.said("slower") or speech.said("slow down"): 
                myShip.slower() 
        elif speech.said("full astern"): 
                myShip.astern100() 
        elif speech.said("astern"): 
                myShip.astern75() 
        elif speech.said("half astern"): 
                myShip.astern50() 
        elif speech.said("slow astern"): 
                myShip.astern25 
        elif speech.said("stop") or speech.said("engines off"): 
                myShip.stop() 
        elif speech.said("slow ahead") or speech.said("go"): 
                myShip.ahead25() 
        elif speech.said("half ahead"): 
                myShip.ahead50() 
        elif speech.said("ahead"): 
                myShip.ahdead75() 
        elif speech.said("full ahead"): 
                myShip.ahead100() 
        elif speech.said("boost") or speech.said("boosters"): 
                myShip.boost() 
        elif speech.said("prepare for super cruise"): 
                myShip.supercruise() 
        elif speech.said("prepare for hyperspace"): 
                myShip.hyperspace() 
        elif speech.said("jump now"): 
                myShip.jump() 
        elif speech.said("disengage frameshift"): 
                myShip.jump() 
        elif speech.said("target") or speech.said("target ahead"): 
                myShip.target() 
        elif speech.said("target next ship") or speech.said("next target"): 
                myShip.targetNext() 
        elif speech.said("target previous ship") or speech.said("previous target"): 
                myShip.targetPrevious() 
        elif speech.said("target threat") or speech.said("target hostile"): 
                myShip.targetHostile() 
        elif speech.said("target next threat") or speech.said("target next hostile"): 
                myShip.targetNextHostile() 
        elif speech.said("target previous threat") or speech.said("target previous hostile"): 
                myShip.targetPreviousHostile() 
        elif speech.said("target next system"): 
                myShip.targetNextSystem() 
        elif speech.said("target previous system"): 
                myShip.targetPreviousSystem() 
        elif speech.said("balance power"): 
                myShip.balancePower() 
        elif speech.said("step engines"): 
                myShip.stepEngines() 
        elif speech.said("step weapons"): 
                myShip.stepWeapons() 
        elif speech.said("step shields") or speech.said("step systems"): 
                myShip.stepShields() 
        elif speech.said("full power to engines"): 
                myShip.fullEngines() 
        elif speech.said("full power to weapons"): 
                myShip.fullWeapons() 
        elif speech.said("full power to shields") or speech.said("full power to systems"): 
                myShip.fullShields() 
        elif speech.said("zoom out") or speech.said("increase range"): 
                myShip.zoomOut() 
        elif speech.said("zoom in") or speech.said("decrease range"): 
                myShip.zoomIn() 
        elif speech.said("no zoom") or speech.said("maximum range"): 
                myShip.maxRange() 
        elif speech.said("full zoom") or speech.said("minimum range"): 
                myShip.minRange() 
        elif speech.said("galaxy map"): 
                myShip.galaxyMap() 
        elif speech.said("system map"): 
                myShip.systemMap() 
                
        elif speech.said("lights are off"): 
                myShip.lights = 0 
                ayAy()
        elif speech.said("lights are on"): 
                myShip.lights = 1
                ayAy()                
        elif speech.said("lights"): 
                myShip.toggleLights() 
        elif speech.said("lights on"): 
                myShip.setLights(1) 
        elif speech.said("lights off"): 
                myShip.setLights(0) 

        elif speech.said("gear is down"): 
                myShip.gear = 1 
                ayAy()
        elif speech.said("gear is up"): 
                myShip.gear = 0
                ayAy()                
        elif speech.said("gear"): 
                myShip.toggleGear() 
        elif speech.said("gear down"): 
                myShip.setGear(1) 
        elif speech.said("gear up"): 
                myShip.setGear(0) 
                
        elif speech.said("hard points are on"): 
                myShip.hardpoints = 1
                ayAy()                
        elif speech.said("hard points are off"): 
                myShip.hardpoints = 0
                ayAy()                
        elif speech.said("hard points"): 
                myShip.toggleHardpoints() 
        elif (speech.said("deploy hard points") or speech.said("attack mode")): 
                myShip.setHardpoints(1) 
        elif speech.said("hide hard points") or speech.said("retract hard points"): 
                myShip.setHardpoints(0) 

        elif speech.said("weapons are selected"): 
                myShip.fireGroup = "weapons"
                ayAy()                
        elif speech.said("scanners are selected"): 
                myShip.fireGroup = "scanners"
                ayAy()                
        elif speech.said("switch to weapons"): 
                myShip.setFireGroup("weapons") 
        elif speech.said("switch to scanners"): 
                myShip.setFireGroup("scanners") 
                
        elif speech.said("scoop is open"): 
                myShip.scoop = 1
                ayAy()                
        elif speech.said("scoop is closed"): 
                myShip.scoop = 0
                ayAy()                
        elif speech.said("open scoop"): 
                myShip.setScoop(1) 
        elif speech.said("close scoop"): 
                myShip.setScoop(0) 
                
        elif speech.said("red alert"): 
                myShip.balancePower 
                myShip.stepShields 
                myShip.stepWeapons 
                myShip.setHardpoints(1) 
                myShip.setFireGroup("weapons") 
                myShip.targetHostile() 
                graj("Requests_AndShowThemThePain") 


# *********************************** 
# Config and commands 
# *********************************** 
if starting: 
    diagnostics.debug("Start")
    myShip = Ship()

#   if(var.time < 0.5) 
#               playsound ("L:\GlovePie2\elite\KICS_GoodMorningCommander.wav") 
#   else: if(var.time < 0.75) 
#               playsound ("L:\GlovePie2\elite\KICS_GoodAfterNoonCommander.wav") 
#   else: 
#               playsound ("L:\GlovePie2\elite\KICS_GoodEveningCommander.wav") 
#   end if 

reguly()