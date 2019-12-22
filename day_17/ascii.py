from stateful_intcode import StatefulIntcode
from coords import Coords, Direction
import re
import random

done_p = re.compile("([A-J,]*)")


def part_one():
    program = [1,330,331,332,109,5242,1101,1182,0,16,1102,1521,1,24,102,1,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,16,1,16,1008,16,1521,570,1006,570,14,21101,0,58,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,73,0,0,1106,0,579,1101,0,0,572,1102,0,1,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,101,0,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,340,1,1,1106,0,177,21101,0,477,1,1106,0,177,21102,1,514,1,21102,176,1,0,1105,1,579,99,21102,184,1,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21101,375,0,1,21101,0,211,0,1105,1,579,21101,1182,11,1,21102,222,1,0,1106,0,979,21102,1,388,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21101,244,0,0,1106,0,979,21101,0,401,1,21102,255,1,0,1105,1,579,21101,1182,33,1,21101,0,266,0,1106,0,979,21102,1,414,1,21102,277,1,0,1106,0,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21101,313,0,0,1105,1,622,1005,575,327,1101,1,0,575,21102,327,1,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,60,24,0,109,4,2101,0,-3,586,21002,0,1,-1,22101,1,-3,-3,21102,1,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,2101,0,-4,629,21002,0,1,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,1,702,0,1106,0,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21101,731,0,0,1106,0,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21102,774,1,0,1106,0,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,20101,0,576,-6,21002,577,1,-5,1105,1,814,21101,0,0,-1,21101,0,0,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,61,-3,22201,-6,-3,-3,22101,1521,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1106,0,924,1205,-2,873,21102,35,1,-4,1106,0,924,2102,1,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1101,2,0,0,2101,0,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,61,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,61,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,1,973,0,1106,0,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21101,-4,0,-2,1106,0,1041,21101,-5,0,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2101,0,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1201,-2,0,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21101,439,0,1,1105,1,1150,21102,1,477,1,1106,0,1150,21102,1,514,1,21101,1149,0,0,1106,0,579,99,21101,1157,0,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,1202,-4,1,0,109,-6,2105,1,0,24,13,48,1,11,1,48,1,11,1,48,1,11,1,48,1,3,13,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,7,42,1,3,1,11,1,1,1,40,7,11,7,36,1,1,1,17,1,3,1,30,9,17,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,7,28,1,5,1,23,1,1,1,28,1,5,1,23,13,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,16,9,25,1,9,1,16,1,1,1,31,1,9,1,10,9,31,13,8,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,2,9,5,1,35,9,2,1,13,1,35,1,10,1,13,1,35,1,10,1,13,1,35,1,10,1,13,13,23,1,10,1,25,1,23,1,10,13,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,17,7,22,1,31,1,28,7,25,1,34,1,25,1,34,1,25,1,34,1,25,1,34,1,17,9,34,1,17,1,42,1,17,1,42,1,17,1,42,7,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,13,24]
    out, done = StatefulIntcode(program, []).run()
    for i in out:
        print(chr(i), end='', flush=True)
    scaffold = dict()
    x = 0
    y = 0
    for i in out:
        if i == 10:
            y += 1
            x = 0
        elif i != ord('.'):
            scaffold[Coords(x, y)] = i
            x += 1
        else:
            x += 1
    intersections = []
    for c in scaffold.keys():
        if all(it in scaffold for it in map(lambda x: c + x, [Coords(0, 1), Coords(0, -1), Coords(1, 0), Coords(-1, 0)])):
            intersections.append(c)
    sum = 0
    for i in intersections:
        sum += i.x * i.y
    print(sum)


def part_two():
    # program = [1,330,331,332,109,5242,1101,1182,0,16,1102,1521,1,24,102,1,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,16,1,16,1008,16,1521,570,1006,570,14,21101,0,58,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,73,0,0,1106,0,579,1101,0,0,572,1102,0,1,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,101,0,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,340,1,1,1106,0,177,21101,0,477,1,1106,0,177,21102,1,514,1,21102,176,1,0,1105,1,579,99,21102,184,1,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21101,375,0,1,21101,0,211,0,1105,1,579,21101,1182,11,1,21102,222,1,0,1106,0,979,21102,1,388,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21101,244,0,0,1106,0,979,21101,0,401,1,21102,255,1,0,1105,1,579,21101,1182,33,1,21101,0,266,0,1106,0,979,21102,1,414,1,21102,277,1,0,1106,0,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21101,313,0,0,1105,1,622,1005,575,327,1101,1,0,575,21102,327,1,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,60,24,0,109,4,2101,0,-3,586,21002,0,1,-1,22101,1,-3,-3,21102,1,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,2101,0,-4,629,21002,0,1,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,1,702,0,1106,0,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21101,731,0,0,1106,0,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21102,774,1,0,1106,0,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,20101,0,576,-6,21002,577,1,-5,1105,1,814,21101,0,0,-1,21101,0,0,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,61,-3,22201,-6,-3,-3,22101,1521,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1106,0,924,1205,-2,873,21102,35,1,-4,1106,0,924,2102,1,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1101,2,0,0,2101,0,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,61,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,61,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,1,973,0,1106,0,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21101,-4,0,-2,1106,0,1041,21101,-5,0,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2101,0,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1201,-2,0,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21101,439,0,1,1105,1,1150,21102,1,477,1,1106,0,1150,21102,1,514,1,21101,1149,0,0,1106,0,579,99,21101,1157,0,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,1202,-4,1,0,109,-6,2105,1,0,24,13,48,1,11,1,48,1,11,1,48,1,11,1,48,1,3,13,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,7,42,1,3,1,11,1,1,1,40,7,11,7,36,1,1,1,17,1,3,1,30,9,17,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,7,28,1,5,1,23,1,1,1,28,1,5,1,23,13,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,16,9,25,1,9,1,16,1,1,1,31,1,9,1,10,9,31,13,8,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,2,9,5,1,35,9,2,1,13,1,35,1,10,1,13,1,35,1,10,1,13,1,35,1,10,1,13,13,23,1,10,1,25,1,23,1,10,13,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,17,7,22,1,31,1,28,7,25,1,34,1,25,1,34,1,25,1,34,1,25,1,34,1,17,9,34,1,17,1,42,1,17,1,42,1,17,1,42,7,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,13,24]
    program = [1,330,331,332,109,5242,1101,1182,0,16,1102,1521,1,24,102,1,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,16,1,16,1008,16,1521,570,1006,570,14,21101,0,58,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,73,0,0,1106,0,579,1101,0,0,572,1102,0,1,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,101,0,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,340,1,1,1106,0,177,21101,0,477,1,1106,0,177,21102,1,514,1,21102,176,1,0,1105,1,579,99,21102,184,1,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21101,375,0,1,21101,0,211,0,1105,1,579,21101,1182,11,1,21102,222,1,0,1106,0,979,21102,1,388,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21101,244,0,0,1106,0,979,21101,0,401,1,21102,255,1,0,1105,1,579,21101,1182,33,1,21101,0,266,0,1106,0,979,21102,1,414,1,21102,277,1,0,1106,0,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21101,313,0,0,1105,1,622,1005,575,327,1101,1,0,575,21102,327,1,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,60,24,0,109,4,2101,0,-3,586,21002,0,1,-1,22101,1,-3,-3,21102,1,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,2101,0,-4,629,21002,0,1,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,1,702,0,1106,0,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21101,731,0,0,1106,0,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21102,774,1,0,1106,0,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,20101,0,576,-6,21002,577,1,-5,1105,1,814,21101,0,0,-1,21101,0,0,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,61,-3,22201,-6,-3,-3,22101,1521,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1106,0,924,1205,-2,873,21102,35,1,-4,1106,0,924,2102,1,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1101,2,0,0,2101,0,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,61,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,61,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,1,973,0,1106,0,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21101,-4,0,-2,1106,0,1041,21101,-5,0,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2101,0,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1201,-2,0,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21101,439,0,1,1105,1,1150,21102,1,477,1,1106,0,1150,21102,1,514,1,21101,1149,0,0,1106,0,579,99,21101,1157,0,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,1202,-4,1,0,109,-6,2105,1,0,24,13,48,1,11,1,48,1,11,1,48,1,11,1,48,1,3,13,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,7,42,1,3,1,11,1,1,1,40,7,11,7,36,1,1,1,17,1,3,1,30,9,17,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,7,28,1,5,1,23,1,1,1,28,1,5,1,23,13,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,16,9,25,1,9,1,16,1,1,1,31,1,9,1,10,9,31,13,8,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,2,9,5,1,35,9,2,1,13,1,35,1,10,1,13,1,35,1,10,1,13,1,35,1,10,1,13,13,23,1,10,1,25,1,23,1,10,13,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,17,7,22,1,31,1,28,7,25,1,34,1,25,1,34,1,25,1,34,1,25,1,34,1,17,9,34,1,17,1,42,1,17,1,42,1,17,1,42,7,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,13,24]
    out, done = StatefulIntcode(program.copy(), []).run()
    for i in out:
        print(chr(i), end='', flush=True)
    scaffold = analyse_scaffold(out)
    robot_coords = next(x for x, y in scaffold.items() if chr(y) in ['^', 'v', '<', '>'])
    directions = {
        '<': Direction(-1, 0),
        '>': Direction(1, 0),
        '^': Direction(0, -1),
        'v': Direction(0, 1)}
    whole_path = ['L']
    scan_whole_path(directions, robot_coords, scaffold, whole_path)
    ngrams = dict()
    for n in range(1, 11):
        for a in range(0, len(whole_path) - n):
            a_routine = routine(whole_path, a, n)
            if a_routine in ngrams.keys() or len(a_routine) > 200:
                continue
            for b in range(a + 1, len(whole_path) - n):
                if whole_path[a:a + n] == whole_path[b:b + n]:
                    b_routine = routine(whole_path, a, n)
                    ngrams[b_routine] = ngrams.get(b_routine, 1) + 1
    routines = dict()
    for a in range(len(whole_path)):
        for b in range(a + 1, len(whole_path)):
            if whole_path[a] == whole_path[b]:
                stop = 0
                while b + stop < len(whole_path) and whole_path[a:a + stop] == whole_path[b:b + stop] and len(routine(whole_path, a, stop)) <= 200 and routine(whole_path, a, stop) not in routines:
                    stop += 1
                b_routine = routine(whole_path, a, stop)
                routines[a] = b_routine
                routines[b] = b_routine
                a +=stop
                break

    whole_path = ','.join(whole_path)
    print(whole_path, len(whole_path))
    ngram_list = list(ngrams.items())

    r_map, remaining = find_optimal_ngrams(ngram_list, whole_path)

    print(r_map)
    print(remaining)
    program[0] = 2
    robot_input = list(map(ord, remaining))
    robot_input = robot_input[0:19]
    robot_input.append(10)
    intcode = StatefulIntcode(program, robot_input)
    intcode.run_and_print()
    for k in range(65, 68):
        robot_input = list(map(ord, r_map[k]))
        robot_input.append(10)
        intcode.cin += robot_input
        intcode.run_and_print()
    intcode.cin += [ord('n'), 10]
    print(intcode.run_and_print())


def find_optimal_ngrams(origin_ngram_list, origin_whole_path, do_print=False):
    origin_ngram_list.sort(key=lambda l: l[1] * len(l[0]), reverse=True)
    origin_ngram_list = list(filter(lambda l: len(l[0]) > 10, origin_ngram_list))
    # origin_ngram_list.sort(key=lambda l: len(l[0]), reverse=True)
    origin_ngram_list = [
        ('L,2,2,2', 1),
        ('R,2,2,2', 1),
        ('2', 1)
    ]
    whole_path = origin_whole_path
    print("ngrams length:", len(origin_ngram_list))
    for ngram in origin_ngram_list:
        print(ngram)
    # while True:
    r_map, remaining = try_combination(do_print, origin_ngram_list, whole_path)
    if len(r_map.keys()) == 3:
        return r_map, remaining


def try_combination(do_print, origin_ngram_list, whole_path):
    ngram_list = origin_ngram_list.copy()
    # random.shuffle(ngram_list)
    # if ngram_list == origin_ngram_list:
    #     raise Exception("already been there :(")
    remaining = whole_path
    sufficient_ngrams = []
    r_map = dict()
    r = ord('A')
    operations = 0
    for ngram in ngram_list:
        if ngram[0] not in remaining:
            continue
        matches_count = len(re.findall(ngram[0], remaining))
        remaining = remaining.replace(ngram[0], chr(r))
        if do_print:
            print("Applied: ", ngram[0], "times", matches_count, "now: ", remaining)
        sufficient_ngrams.append(ngram)
        r_map[r] = ngram[0]
        operations += matches_count
        r += 1
        if done_p.search(remaining).group(1) == remaining:
            return r_map, remaining
        elif len(r_map.keys()) > 3:
            return dict(), remaining
    return dict(), remaining


def scan_whole_path(directions, robot_coords, scaffold, whole_path):
    scanner = Scanner(scaffold, robot_coords, directions.get('<'))
    i = 0
    while True:
        if scanner.lookup():
            i += 1
            scanner.move()
            if i >= 2:
                whole_path.append(str(i))
                i = 0
        else:
            if i > 0:
                whole_path.append(str(i))
                i = 0
            if scanner.lookup_at_direction(scanner.direction.turnLeft()):
                whole_path.append('L')
                scanner.direction = scanner.direction.turnLeft()
            elif scanner.lookup_at_direction(scanner.direction.turnRight()):
                whole_path.append('R')
                scanner.direction = scanner.direction.turnRight()
            else:
                break


def routine(whole_path, i, stop):
    return ','.join(whole_path[i:i+stop])

class Scanner:
    def __init__(self, scaffold, robot_coords, robot_direction):
        self.direction = robot_direction
        self.position = robot_coords
        self.scaffold = scaffold

    def lookup_at_direction(self, direction):
        return chr(self.scaffold.get(self.position + direction, ord('.'))) == '#'

    def lookup(self):
        return self.lookup_at_direction(self.direction)

    def move(self):
        self.position += self.direction


def analyse_scaffold(out):
    scaffold = dict()
    x = 0
    y = 0
    for i in out:
        if is_line_break(i):
            y += 1
            x = 0
        elif i != ord('.'):
            scaffold[Coords(x, y)] = i
            x += 1
        else:
            x += 1
    return scaffold


def is_line_break(i):
    return i == 10


if __name__ == '__main__':
    print(','.join(list(map(lambda x:str(ord(x)), "Definitions may be at most 20 characters!"))))
    # text = list(map(ord, "Definitions may be at most 20 characters!"))
    # program = [2,330,331,332,109,5242,1101,1182,0,16,1102,1521,1,24,102,1,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,16,1,16,1008,16,1521,570,1006,570,14,21101,0,58,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,73,0,0,1106,0,579,1101,0,0,572,1102,0,1,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,101,0,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1105,1,81,21102,340,1,1,1106,0,177,21101,0,477,1,1106,0,177,21102,1,514,1,21102,176,1,0,1105,1,579,99,21102,184,1,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,102,1,572,1182,21101,375,0,1,21101,0,211,0,1105,1,579,21101,1182,11,1,21102,222,1,0,1106,0,979,21102,1,388,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21101,244,0,0,1106,0,979,21101,0,401,1,21102,255,1,0,1105,1,579,21101,1182,33,1,21101,0,266,0,1106,0,979,21102,1,414,1,21102,277,1,0,1106,0,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21101,313,0,0,1105,1,622,1005,575,327,1101,1,0,575,21102,327,1,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,60,24,0,109,4,2101,0,-3,586,21002,0,1,-1,22101,1,-3,-3,21102,1,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,2101,0,-4,629,21002,0,1,-2,22101,1,-4,-4,21102,1,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21102,1,702,0,1106,0,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21101,731,0,0,1106,0,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1105,1,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21102,774,1,0,1106,0,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,20101,0,576,-6,21002,577,1,-5,1105,1,814,21101,0,0,-1,21101,0,0,-5,21102,0,1,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,61,-3,22201,-6,-3,-3,22101,1521,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1106,0,924,1205,-2,873,21102,35,1,-4,1106,0,924,2102,1,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1101,2,0,0,2101,0,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,61,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,61,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,1,973,0,1106,0,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21101,-4,0,-2,1106,0,1041,21101,-5,0,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2101,0,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1201,-2,0,0,1105,1,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21101,439,0,1,1105,1,1150,21102,1,477,1,1106,0,1150,21102,1,514,1,21101,1149,0,0,1106,0,579,99,21101,1157,0,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,1202,-4,1,0,109,-6,2105,1,0,24,13,48,1,11,1,48,1,11,1,48,1,11,1,48,1,3,13,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,1,3,1,44,1,3,1,7,7,42,1,3,1,11,1,1,1,40,7,11,7,36,1,1,1,17,1,3,1,30,9,17,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,1,3,1,30,1,5,1,19,7,28,1,5,1,23,1,1,1,28,1,5,1,23,13,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,18,1,5,1,25,1,9,1,16,9,25,1,9,1,16,1,1,1,31,1,9,1,10,9,31,13,8,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,10,1,5,1,43,1,2,9,5,1,35,9,2,1,13,1,35,1,10,1,13,1,35,1,10,1,13,1,35,1,10,1,13,13,23,1,10,1,25,1,23,1,10,13,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,23,1,22,1,13,1,17,7,22,1,31,1,28,7,25,1,34,1,25,1,34,1,25,1,34,1,25,1,34,1,17,9,34,1,17,1,42,1,17,1,42,1,17,1,42,7,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,1,11,1,48,13,24]

    part_two()
    exit()