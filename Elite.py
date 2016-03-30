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

def said(what):
    speech.said(what,0.7)

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
    silentrun = 0

    def dump(self):
        diagnostics.debug("==============================")
        diagnostics.debug("gear %d" % self.gear)
        diagnostics.debug("ligh %d" % self.lights)
        diagnostics.debug("fire %s" % self.fireGroup)
        diagnostics.debug("scoo %d" % self.scoop)
        diagnostics.debug("hard %d" % self.hardpoints)
        diagnostics.debug("pane %s" % self.panel)
        diagnostics.debug("sile %d" % self.silentrun)


    def toggleSilentRunning(self):
        if (self.silentrun == 0):
            self.setSilentRunning(1)
        else:
            self.setSilentRunning(0)

    def setSilentRunning(self, state):
        if (self.silentrun != state):
            KeyPress(Key.Delete)
            if (state == 1):
                wav("Cooling_SilentRunning")
            else:
                wav("Cooling_RestoringHeatSignature")
            self.silentrun = state
        self.dump()

    def leftPanel(self):
        if(self.panel != "left"):
            self.panel = "left"
            KeyPress(Key.D1)
            wait(1)
        self.dump()

    def deployHeatSink(self):
        KeyPress(Key.O)
        wav("Cooling_HeatsinkDeployed")

    def targetWingman1(self):
        KeyPress(Key.D7)
        wav("Targeting_Wingman1")


    def targetWingman2(self):
        KeyPress(Key.D8)
        wav("Targeting_Wingman2")


    def targetWingman3(self):
        KeyPress(Key.D9)
        wav("Targeting_Wingman3")


    def targetWingmanTarget(self):
        KeyPress(Key.D0)
        wav("Targeting_WingmansTarget")


    def engageWingmanNavLock(self):
        KeyPress(Key.Minus)
        wav("Targeting_WingmanNavLockEngaging")

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
    
    if said("computer"):
        sayWhat()
        listening = 1
    if said("stop listening"):
        sayAyAy()
        listening = 0

    if listening:
        if said("thank you"):
            sayYoureWelcome()
        elif said("hello"):
            wav("KICS_HelloCommander")
        elif said("can you hear me"):
            wav("KICS_LoudAndClear")

        elif said("faster") or said("speed up"):
            myShip.faster()
        elif said("slower") or said("slow down"):
            myShip.slower()
        elif said("full astern"):
            myShip.astern100()
        elif said("astern"):
            myShip.astern75()
        elif said("half astern"):
            myShip.astern50()
        elif said("slow astern"):
            myShip.astern25
        elif said("stop") or said("engines off"):
            myShip.stop()
        elif said("slow ahead"):
            myShip.ahead25()
        elif said("half ahead"):
            myShip.ahead50()
        elif said("ahead"):
            myShip.ahdead75()
        elif said("full ahead"):
            myShip.ahead100()
        elif said("boost") or said("boosters"):
            myShip.boost()
        elif said("prepare for super cruise"):
            myShip.supercruise()
        elif said("prepare for hyperspace"):
            myShip.hyperspace()
        elif said("jump now"):
            myShip.toggleFrameShift()
            wav("FlightMisc_EngagingFrameShiftDrive")
        elif said("disengage frameshift"):
            myShip.toggleFrameShift()
            wav("FlightMisc_Disengaging")
        elif said("target") or said("target ahead"):
            myShip.target()
        elif said("target next ship") or said("next target"):
            myShip.targetNext()
        elif said("target previous ship") or said("previous target"):
            myShip.targetPrevious()
        elif said("target threat") or said("target hostile"):
            myShip.targetHostile()
        elif said("target next threat") or said("target next hostile"):
            myShip.targetNextHostile()
        elif said("target previous threat") or said("target previous hostile"):
            myShip.targetPreviousHostile()
        elif said("target next system"):
            myShip.targetNextSystem()
        elif said("target previous system"):
            myShip.targetPreviousSystem()
        elif said("balance power"):
            myShip.balancePower()
        elif said("step engines"):
            myShip.stepEngines()
        elif said("step weapons"):
            myShip.stepWeapons()
        elif said("step shields") or said("step systems"):
            myShip.stepShields()
        elif said("full power to engines"):
            myShip.fullEngines()
        elif said("full power to weapons"):
            myShip.fullWeapons()
        elif said("full power to shields") or said("full power to systems"):
            myShip.fullShields()
        elif said("zoom out") or said("increase range"):
            myShip.zoomOut()
        elif said("zoom in") or said("decrease range"):
            myShip.zoomIn()
        elif said("no zoom") or said("maximum range"):
            myShip.maxRange()
        elif said("full zoom") or said("minimum range"):
            myShip.minRange()
        elif said("galaxy map"):
            myShip.galaxyMap()
        elif said("system map"):
            myShip.systemMap()

        elif said("lights are off"):
            myShip.lights = 0
            sayAyAy()
        elif said("lights are on"):
            myShip.lights = 1
            sayAyAy()
        elif said("lights"):
            myShip.toggleLights()
        elif said("lights on"):
            myShip.setLights(1)
        elif said("lights off"):
            myShip.setLights(0)

        elif said("gear is down"):
            myShip.gear = 1
            sayAyAy()
        elif said("gear is up"):
            myShip.gear = 0
            sayAyAy()
        elif said("gear"):
            myShip.toggleGear()
        elif said("gear down"):
            myShip.setGear(1)
        elif said("gear up"):
            myShip.setGear(0)

        elif said("hard points are on"):
            myShip.hardpoints = 1
            sayAyAy()
        elif said("hard points are off"):
            myShip.hardpoints = 0
            sayAyAy()
        elif said("hard points"):
            myShip.toggleHardpoints()
        elif (said("deploy hard points") or said("attack mode")):
            myShip.setHardpoints(1)
        elif said("hide hard points") or said("retract hard points"):
            myShip.setHardpoints(0)

        elif said("weapons are selected"):
            myShip.fireGroup = "weapons"
            sayAyAy()
        elif said("scanners are selected"):
            myShip.fireGroup = "scanners"
            sayAyAy()
        elif said("switch to weapons"):
            myShip.setFireGroup("weapons")
        elif said("switch to scanners"):
            myShip.setFireGroup("scanners")

        elif said("scoop is open"):
            myShip.scoop = 1
            sayAyAy()
        elif said("scoop is closed"):
            myShip.scoop = 0
            sayAyAy()
        elif said("open scoop"):
            myShip.setScoop(1)
        elif said("close scoop"):
            myShip.setScoop(0)

        elif said("red alert"):
            myShip.balancePower
            myShip.stepShields
            myShip.stepWeapons
            myShip.setHardpoints(1)
            myShip.setFireGroup("weapons")
            myShip.targetHostile()
            wav("Requests_AndShowThemThePain")
            
        elif said("request docking"):
            myShip.leftPanel()
            myShip.nextPanelTab()
            myShip.nextPanelTab()
            myShip.panelEnter()
            myShip.cursorDown()
            myShip.panelEnter()
            myShip.prevPanelTab()
            myShip.prevPanelTab()
            myShip.noPanel()

        elif said("no panel"):
            myShip.noPanel()

        elif said("silent running"):
            myShip.toggleSilentRunning()
        elif said("silent running on"):
            myShip.setSilentRunning(1)
        elif said("silent running off"):
            myShip.setSilentRunning(0)
        elif said("request docking"):
            myShip.requestDock()
        elif said("deploy heat sink"):
            myShip.deployHeatSink()
        elif said("target wingman one"):
            myShip.targetWingman1()
        elif said("target wingman two"):
            myShip.targetWingman2()
        elif said("target wingman three"):
            myShip.targetWingman3()
        elif said("target wingmans target"):
            myShip.targetWingmanTarget()
        elif said("engage wingman nav lock"):
            myShip.engageWingmanNavLock()

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
