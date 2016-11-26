import time
import os
from mido import MidiFile

import readmidi_nn
import data_set_nn

from pyPlayMusic import pyPlayMusic

playlist = readmidi_nn.readmidi("/sampleMidi/moonlight.mid")
"""
for play in playlist:
    #print play
    pyPlayMusic.playNotes(play).play()
    time.sleep(160/480.)
"""
x,y = readmidi_nn.makeMidi_nn(playlist,24)

batch = data_set_nn.data_set_nn(x,y)

batchX, batchY = batch.get_next_batch(size=100)

c = []

c1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
c2 = [[], [43], [], [38], [43], [47], [], [45], [47], [], [43], [], [], [45], [47], [42], [45], [47], [], [47], [52], [43], [47], [52], [], [45], [48], [], [45], [48], [], [45], [], [], [45], [47], [], [43], [47], [40], [43], [47], [40], [], [47], [], [44], [47], [], [45], [48], [], [45], [48], [], [45], [48], [], [45], [48], [], [44], [47], [40], [44], [47], [], [], [], [], [], [47], [], [45], [48], [], [45], [48], [], [45], [48], [], [45], [48], [], [44], [47], [40], [44], [47], [], [], [], [], [], [48], [], [45], [48], [38]]
c3 = [[34], [38], [44], [34], [38], [44], [], [38], [44], [46], [], [39], [43], [], [38], [43], [], [40], [43], [], [40], [43], [], [38], [41], [33], [38], [41], [], [38], [40], [], [38], [40], [], [38], [41], [33], [38], [41], [], [37], [40], [33], [37], [40], [], [41], [45], [38], [41], [45], [38], [42], [45], [], [42], [45], [], [43], [46], [], [43], [46], [], [43], [46], [], [43], [46], [], [42], [45], [38], [42], [45], [], [], [], [], [42], [45], [], [43], [46], [], [43], [46], [], [43], [46], [], [43], [46], [], [42], [45], [38], [42], [45]]
c4 = [[35], [36], [35], [33], [], [31], [40], [28], [31], [40], [], [36], [40], [30], [36], [40], [], [35], [39], [30], [33], [39], [], [35], [40], [35], [40], [43], [35], [40], [43], [], [40], [43], [47], [], [42], [45], [35], [42], [45], [35], [42], [45], [], [42], [45], [47], [], [40], [43], [35], [40], [43], [], [40], [45], [36], [40], [45], [], [38], [43], [35], [38], [43], [], [38], [42], [], [38], [42], [], [38], [43], [], [], [47], [38], [43], [47], [], [43], [47], [50], [], [45], [48], [38], [45], [48], [38], [45], [48], [], [45], [48], [50], [], [43]]
c5 = [[40], [43], [], [41], [45], [36], [41], [45], [], [39], [45], [35], [40], [43], [], [40], [42], [33], [39], [42], [], [35], [40], [35], [40], [43], [35], [40], [43], [], [40], [43], [47], [], [42], [45], [35], [42], [45], [35], [42], [45], [], [42], [45], [47], [], [40], [43], [35], [40], [43], [], [40], [45], [36], [40], [45], [], [38], [43], [35], [38], [43], [], [38], [42], [], [38], [42], [], [38], [43], [], [], [43], [35], [38], [43], [35], [38], [43], [], [38], [43], [34], [38], [43], [34], [38], [43], [], [38], [43], [46], [], [38], [44], [34], [38]]
c6 = [[], [36], [33], [39], [36], [42], [39], [45], [42], [48], [45], [51], [], [40], [35], [43], [40], [47], [43], [52], [47], [55], [52], [47], [], [46], [43], [49], [46], [52], [49], [55], [52], [58], [55], [61], [], [51], [48], [54], [51], [57], [54], [60], [57], [63], [60], [66], [63], [57], [60], [54], [57], [51], [54], [48], [51], [45], [48], [42], [45], [39], [42], [36], [39], [33], [36], [30], [33], [28], [33], [36], [], [33], [35], [36], [35], [33], [30], [33], [36], [28], [33], [36], [], [33], [35], [36], [35], [33], [29], [33], [36], [28], [33], [36], [], [33], [35], [36]]
c7 = [[40], [43], [23], [], [42], [45], [35], [42], [45], [35], [42], [45], [], [42], [45], [23], [], [43], [40], [47], [43], [52], [47], [55], [52], [], [55], [52], [23], [], [54], [48], [51], [45], [48], [42], [45], [36], [], [35], [33], [23], [], [], [40], [47], [43], [52], [47], [55], [52], [], [55], [52], [23], [], [54], [48], [51], [45], [48], [42], [45], [36], [], [35], [33], [23], [], [], [40], [43], [40], [35], [28], [31], [35], [40], [35], [31], [23], [28], [31], [35], [31], [28], [23], [28], [23], [19], [23], [19], [16], [], [], [40], [43], [36], [40], [43]]
c8 = [[52], [], [47], [50], [40], [47], [50], [40], [47], [50], [], [47], [50], [52], [], [45], [48], [40], [45], [48], [], [45], [48], [], [45], [48], [], [45], [47], [42], [45], [47], [42], [45], [47], [], [45], [47], [], [47], [52], [43], [47], [52], [], [45], [48], [], [43], [49], [], [39], [42], [47], [39], [42], [48], [39], [42], [45], [39], [42], [], [39], [42], [35], [39], [42], [36], [39], [42], [33], [39], [42], [], [43], [47], [52], [43], [47], [55], [43], [47], [52], [43], [47], [], [31], [35], [40], [31], [35], [43], [31], [35], [40], [31], [35], [], [36]]
c9 = [[48], [], [45], [48], [], [44], [47], [40], [44], [47], [], [44], [47], [], [44], [47], [], [45], [48], [], [45], [48], [], [45], [48], [], [45], [48], [], [44], [47], [40], [44], [47], [], [45], [48], [40], [45], [48], [], [45], [48], [38], [45], [48], [38], [45], [48], [], [43], [47], [], [43], [47], [], [42], [45], [], [42], [45], [], [40], [43], [], [40], [42], [33], [40], [42], [], [40], [42], [], [40], [42], [], [40], [43], [35], [40], [43], [], [39], [42], [33], [39], [42], [], [35], [40], [35], [40], [43], [35], [40], [43], [], [40], [43]]
c10 = [[42], [45], [], [43], [46], [], [43], [46], [], [43], [46], [], [43], [46], [], [42], [45], [38], [42], [45], [], [42], [45], [], [42], [45], [], [43], [46], [], [43], [46], [], [43], [46], [], [43], [46], [], [42], [45], [38], [42], [45], [], [41], [44], [38], [41], [44], [], [40], [47], [38], [40], [47], [], [40], [45], [36], [40], [45], [], [38], [41], [34], [38], [41], [], [36], [42], [33], [36], [42], [], [33], [36], [28], [33], [36], [], [33], [35], [], [32], [35], [], [36], [40], [36], [40], [45], [40], [45], [48], [], [45], [48], [52], []]
c11 = [[], [46], [49], [], [45], [48], [41], [45], [48], [], [45], [48], [], [45], [48], [], [46], [49], [], [46], [49], [], [46], [49], [], [46], [49], [], [45], [48], [41], [45], [48], [], [46], [49], [41], [46], [49], [], [46], [49], [39], [46], [49], [39], [46], [49], [], [44], [48], [], [44], [48], [], [43], [46], [], [43], [46], [], [41], [44], [], [41], [43], [34], [41], [43], [], [41], [43], [], [41], [43], [], [41], [44], [36], [41], [44], [], [40], [43], [34], [40], [43], [], [36], [41], [36], [41], [44], [36], [41], [44], [], [41], [44], [24], [], [43], [46], [36], [43], [46], [36], [43], [46], [], [43], [46], [24], [], [44], [41], [48], [44], [53], [48], [56], [53], [], [56], [53], [24], [], [55], [49], [52], [46], [49], [43], [46], [37], [], [36], [34], [24], [], [], [41], [48], [44], [53], [48], [56], [53], [], [56], [53], [24], [], [55], [49], [52], [46], [49], [43], [46], [37], [], [36], [34], [24], [], [], [41], [44], [41], [36], [29], [32], [36], [41], [36], [32], [24], [29], [32], [36], [32], [29], [24], [29], [24], [20], [24], [20], [17], [], [], [41], [44], [37], [41], [44], [], [42], [46], [37], [42], [46], [], [40], [46], [36], [41], [44], [], [41], [43], [34], [40], [43], [], [36], [41], [36], [41], [44], [36], [41], [44], [], [41], [44], [48], [], [43], [46], [36], [43], [46], [36], [43], [46], [], [43], [46], [48], [], [41], [44], [36], [41], [44], [], [41], [46]]
#c11의 정확성은 5%입니다.
b1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
b2 = [[51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50]]
b3 = [[48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48]]
b4 = [[54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43]]
b5 = [[55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50]]
b6 = [[53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48]]
b7 = [[54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [47], [50], [51], [43], [55], [54], [55], [54], [55], [50], [53], [51], [48], [39], [43], [48], [50], [43], [51], [50], [48], [], [51], [53], [55], [46], [56], [55], [53], [44], [55], [53], [51], [43], [53], [51], [50], [43], [55], [54]]

"""
#batchY
for i in batchY:
    a = []
    for j in range(len(i)):
        if i[j] == 1:
            a.append(j)
    print a
    pyPlayMusic.playNotes(a).play()
    time.sleep(160 / 480.)
"""

print "learn 100 * 10000"

for i in c10:

    if i != []:
        pyPlayMusic.playNotes(i).play()
        time.sleep(160 / 480.)
