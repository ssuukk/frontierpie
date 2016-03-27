import time;
from ctypes import *;
from random import randint

# ***********************************
# Config
# ***********************************
# change to the path you keep your wav files
soundDir = 'L:\GlovePie2\Elite\%s.wav'


# *********************************** 
# MCI audio playback
# *********************************** 
winmm = windll.winmm

def mciSend(s):
    i = winmm.mciSendStringW(s, None, 0, 0)
    if i <> 0:
        diagnostics.debug("Error %d in mciSendString %s" % (i, s))

# mp3 does not work for me, your mileage may vary
def mciPlayBlocking(mp3Name):
    mciSend('Close All')
    # mciSend("Open \"%s\" Type MPEGVideo Alias theMP3" % mp3Name)
    mciSend("Open \"%s\" Type Waveaudio Alias theMP3" % mp3Name)
    mciSend("Play theMP3 Wait")
    mciSend("Close theMP3")

def wav(name):
    mciPlayBlocking(soundDir % name)

# ***********************************
# misc utility functions
# ***********************************
def wait(duration):
    clock = time.time()
    while time.time() < (clock + duration):
        diagnostics.debug("wait")
        pass

def KeyPress(key):
    keyboard.setKeyDown(key)
    wait(0.07)
    keyboard.setKeyUp(key)

def KeyRepeat(key, times):
    for num in range(1, times):
        KeyPress(key)
        wait(0.1)

# ***********************************
# your ship
# ***********************************
class Ship:
    # assuming we start with gear down
    gear = 1
    lights = 0
    # my config uses two fire groups, one for weapons, another for scanners
    # this way you can command your ship to either change to wepons or scanners
    fireGroup = "weapons"
    scoop = 0
    hardpoints = 0
    panel = "none"

    def dump(self):
        diagnostics.debug("==============================")
        diagnostics.debug("gear %d" % self.gear)
        diagnostics.debug("ligh %d" % self.lights)
        diagnostics.debug("fire %s" % self.fireGroup)
        diagnostics.debug("scoo %d" % self.scoop)
        diagnostics.debug("hard %d" % self.hardpoints)
        diagnostics.debug("pane %s" % self.panel)

    def leftPanel(self):
        if(self.panel != "left"):
            self.panel = "left"
            KeyPress(Key.D1)
            wait(1)
        self.dump()

    def bottomPanel(self):
        if(self.panel != "bottom"):
            self.panel = "bottom"
            KeyPress(Key.D2)
            wait(1)
        self.dump()
        
    def rightPanel(self):
        if(self.panel != "right"):
            self.panel = "right"
            KeyPress(Key.D3)
            wait(1)
        self.dump()
        
    def noPanel(self):
        if(self.panel != "none"):
            self.panel = "none"
            KeyPress(Key.Backspace)
            wait(1)
        self.dump()
        
    def nextPanelTab(self):
        if(self.panel != "none"):
            KeyPress(Key.E)
            wait(0.3)
        
    def prevPanelTab(self):
        if(self.panel != "none"):
            KeyPress(Key.Q)
            wait(0.3)

    def cursorLeft(self):
        if(self.panel != "none"):
            KeyPress(Key.A)
            wait(0.3)

    def cursorRight(self):
        if(self.panel != "none"):
            KeyPress(Key.D)
            wait(0.3)

    def cursorUp(self):
        if(self.panel != "none"):
            KeyPress(Key.W)
            wait(0.3)

    def cursorDown(self):
        if(self.panel != "none"):
            KeyPress(Key.S)
            wait(0.3)

    def panelEnter(self):
        if(self.panel != "none"):
            KeyPress(Key.Space)
            wait(0.3)

    def panelBack(self):
        if(self.panel != "none"):
            KeyPress(Key.Backspace)
            wait(0.3)

    def toggleGear(self):
        if (self.gear == 0):
            self.setGear(1)
        else:
            self.setGear(0)

    def setGear(self, state):
        if (self.gear != state):
            KeyPress(Key.I)
            if (state == 1):
                wav("Misc_ActivatingLandingGear")
            else:
                wav("Misc_DeactivatingLandingGear")
            self.gear = state
        self.dump()

    def toggleLights(self):
        if (self.lights == 0):
            self.setLights(1)
        else:
            self.setLights(0)

    def setLights(self, state):
        if (self.lights != state):
            KeyPress(Key.L)
            if (state == 1):
                wav("Misc_Illuminating")
            else:
                wav("Misc_Deluminating")
            self.lights = state
        self.dump()

    def setFireGroup(self, state):
        if (self.fireGroup != state):
            if (state == "weapons"):
                wav("KICS_Weapons")
                KeyPress(Key.B)
            else:
                wav("Driving_ActivatingDataLinkScanner")
                KeyPress(Key.N)
            self.fireGroup = state
        self.dump()

    def toggleScoop(self):
        if (self.scoop == 0):
            self.setScoop(1)
        else:
            self.setScoop(0)

    def setScoop(self, state):
        if (self.scoop != state):
            if (state == 1):
                wav("Misc_ActivatingCargoScoop")
            else:
                wav("Misc_DeactivatingCargoScoop")
            self.scoop = state
        self.dump()

    def toggleHardpoints(self):
        if (self.hardpoints == 0):
            self.setHardpoints(1)
        else:
            self.setHardpoints(0)

    def setHardpoints(self, state):
        if (self.hardpoints != state):
            KeyPress(Key.U)
            if (state == 1):
                wav("Weapons_DeployingHardpoints")
            else:
                wav("Weapons_RetractingHardpoints")
            self.hardpoints = state
        self.dump()

    def faster(self):
        KeyPress(Key.W)
        wav("FlightThrottle_IncreasingVelocity")

    def slower(self):
        KeyPress(Key.S)
        wav("FlightThrottle_DecreasingVelocity")

    def astern100(self):
        KeyPress(Key.NumberPad1)
        wav("FlightThrottle_Negative100")

    def astern75(self):
        KeyPress(Key.NumberPad2)
        wav("FlightThrottle_Negative75")

    def astern50(self):
        KeyPress(Key.NumberPad3)
        wav("FlightThrottle_Negative50")

    def astern25(self):
        KeyPress(Key.NumberPad4)
        wav("FlightThrottle_Negative25")

    def stop(self):
        KeyPress(Key.NumberPad5)
        wav("FlightThrottle_Stopping")

    def ahead25(self):
        KeyPress(Key.NumberPad6)
        wav("FlightThrottle_Throttle25")

    def ahead50(self):
        KeyPress(Key.NumberPad7)
        wav("FlightThrottle_Throttle50")

    def ahdead75(self):
        KeyPress(Key.NumberPad8)
        wav("FlightThrottle_Throttle75")

    def ahead100(self):
        KeyPress(Key.NumberPad9)
        wav("FlightThrottle_MaximumVelocity")

    def boost(self):
        KeyPress(Key.Tab)
        wav("FlightMisc_EngagingBoost")

    def supercruise(self):
        KeyPress(Key.Comma)
        wav("FlightMisc_ActivatingSupercruise")

    def hyperspace(self):
        KeyPress(Key.Period)
        wav("FlightMisc_PreparingForHyperspaceTravel")

    def toggleFrameShift(self):
        KeyPress(Key.J)

    def target(self):
        KeyPress(Key.T)
        wav("Targeting_LockingTarget")

    def targetNext(self):
        KeyPress(Key.G)
        wav("Targeting_TargetingNext")

    def targetPrevious(self):
        KeyPress(Key.D5)
        wav("Targeting_TargetingPrevious")

    def targetHostile(self):
        KeyPress(Key.H)
        wav("Targeting_TargetingHighestThreat")

    def targetNextHostile(self):
        KeyPress(Key.D7)
        wav("Targeting_TargetingNextHostile")

    def targetPreviousHostile(self):
        KeyPress(Key.D6)
        wav("Targeting_TargetingNextHostile")

    def targetNextSystem(self):
        KeyPress(Key.D0)
        wav("Targeting_TargetingNextSystem")

    def targetPreviousSystem(self):
        KeyPress(Key.D9)
        wav("Targeting_TargetingPreviousSystem")

    def balancePower(self):
        KeyPress(Key.DownArrow)
        wav("KICS_Balancing")

    def stepEngines(self):
        KeyPress(Key.UpArrow)
        wav("KICS_AdjustingPower")

    def stepWeapons(self):
        KeyPress(Key.RightArrow)
        wav("KICS_AdjustingPower")

    def stepShields(self):
        KeyPress(Key.LeftArrow)
        wav("KICS_AdjustingPower")

    def fullEngines(self):
        KeyRepeat(Key.UpArrow, 5)
        wav("KICS_AdjustingPower")

    def fullWeapons(self):
        KeyRepeat(Key.RightArrow, 5)
        wav("KICS_AdjustingPower")

    def fullShields(self):
        KeyRepeat(Key.LeftArrow, 5)
        wav("KICS_AdjustingPower")

    def zoomIn(self):
        KeyPress(Key.PageUp)
        wav("Misc_IncreasingSensorRange")

    def zoomOut(self):
        KeyPress(Key.PageDown)
        wav("Misc_DecreasingSensorRange")

    def maxRange(self):
        KeyRepeat(Key.PageUp, 8)
        wav("Misc_MaximisingSensorRange")

    def minRange(self):
        KeyRepeat(Key.PageDown, 8)
        wav("Misc_MinimisingSensorRange")

    def galaxyMap(self):
        KeyPress(Key.M)
        wav("ModeSwitches_AccessingGalaxyMap")

    def systemMap(self):
        KeyPress(Key.O)
        wav("ModeSwitches_AccessingSystemMap")

# ***********************************
# a few pre-cooked responses
# ***********************************
def sayYoureWelcome():
    r = randint(1, 4)
    if r == 1:
        wav("KICS_YouAreMostWelcome")
    elif r == 2:
        wav("KICS_Anytime")
    elif r == 3:
        wav("KICS_AnytimeCommander")
    elif r == 4:
        wav("KICS_YouAreWelcome")


def sayWhat():
    r = randint(1, 4)
    if r == 1:
        wav("KICS_YesCommanderQ")
    elif r == 2:
        wav("KICS_YesQ")
    elif r == 3:
        wav("KICS_WhatIsItCommander")
    elif r == 4:
        wav("KICS_HmmmQ")


def sayAyAy():
    r = randint(1, 7)
    if r == 1:
        wav("KICS_AsYouWish")
    elif r == 2:
        wav("KICS_AyeAye")
    elif r == 3:
        wav("KICS_AyeCommander")
    elif r == 4:
        wav("KICS_Certainly")
    elif r == 5:
        wav("KICS_CertainlyCommander")
    elif r == 6:
        wav("KICS_Done")
    elif r == 7:
        wav("KICS_DoneCommander")

# ***********************************
# rules
# ***********************************
def voiceCommands():
    global listening
    
    if speech.said("computer"):
        sayWhat()
        listening = 1
    if speech.said("stop listening"):
        sayAyAy()
        listening = 0

    if listening:
        if speech.said("thank you"):
            sayYoureWelcome()
        elif speech.said("hello"):
            wav("KICS_HelloCommander")
        elif speech.said("can you hear me"):
            wav("KICS_LoudAndClear")

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
            myShip.toggleFrameShift()
            wav("FlightMisc_EngagingFrameShiftDrive")
        elif speech.said("disengage frameshift"):
            myShip.toggleFrameShift()
            wav("FlightMisc_Disengaging")
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
            sayAyAy()
        elif speech.said("lights are on"):
            myShip.lights = 1
            sayAyAy()
        elif speech.said("lights"):
            myShip.toggleLights()
        elif speech.said("lights on"):
            myShip.setLights(1)
        elif speech.said("lights off"):
            myShip.setLights(0)

        elif speech.said("gear is down"):
            myShip.gear = 1
            sayAyAy()
        elif speech.said("gear is up"):
            myShip.gear = 0
            sayAyAy()
        elif speech.said("gear"):
            myShip.toggleGear()
        elif speech.said("gear down"):
            myShip.setGear(1)
        elif speech.said("gear up"):
            myShip.setGear(0)

        elif speech.said("hard points are on"):
            myShip.hardpoints = 1
            sayAyAy()
        elif speech.said("hard points are off"):
            myShip.hardpoints = 0
            sayAyAy()
        elif speech.said("hard points"):
            myShip.toggleHardpoints()
        elif (speech.said("deploy hard points") or speech.said("attack mode")):
            myShip.setHardpoints(1)
        elif speech.said("hide hard points") or speech.said("retract hard points"):
            myShip.setHardpoints(0)

        elif speech.said("weapons are selected"):
            myShip.fireGroup = "weapons"
            sayAyAy()
        elif speech.said("scanners are selected"):
            myShip.fireGroup = "scanners"
            sayAyAy()
        elif speech.said("switch to weapons"):
            myShip.setFireGroup("weapons")
        elif speech.said("switch to scanners"):
            myShip.setFireGroup("scanners")

        elif speech.said("scoop is open"):
            myShip.scoop = 1
            sayAyAy()
        elif speech.said("scoop is closed"):
            myShip.scoop = 0
            sayAyAy()
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
            wav("Requests_AndShowThemThePain")
            
        elif speech.said("request docking"):
            myShip.leftPanel()
            myShip.nextPanelTab()
            myShip.nextPanelTab()
            myShip.panelEnter()
            myShip.cursorDown()
            myShip.panelEnter()
            myShip.prevPanelTab()
            myShip.prevPanelTab()
            myShip.noPanel()

        elif speech.said("no panel"):
            myShip.noPanel()

def androidHeadTracking():
    #Apply deadband filter to avoid drift
    #And continousRotation filter to yaw axis to avoid jumps when passing tracker center
    deadband = 0.01

    x = filters.deadband(filters.delta(math.degrees(filters.continousRotation(android[0].googlePitch))), deadband)
    y = filters.deadband(filters.delta(math.degrees(android[0].googleRoll)), deadband)

    mouse.deltaX = x * 20
    mouse.deltaY = y * 5


# *********************************** 
# Config and commands 
# *********************************** 
if starting:
    diagnostics.debug("Start")
    myShip = Ship()

    # if should start listening
    listening = 1

    # uncomment to enable Android head tracking
    #android[0].update += androidHeadTracking

# if(var.time < 0.5)
#               playsound ("L:\GlovePie2\elite\KICS_GoodMorningCommander.wav") 
#   else: if(var.time < 0.75) 
#               playsound ("L:\GlovePie2\elite\KICS_GoodAfterNoonCommander.wav") 
#   else: 
#               playsound ("L:\GlovePie2\elite\KICS_GoodEveningCommander.wav") 
#   end if 

voiceCommands()
