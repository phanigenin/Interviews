import sys

# String constant settings
TRIP_MARKER = '0'
UP_SIGNAL   = 'UP'
DN_SIGNAL   = 'DN'

# Elevator Mode settings
SIMPLE_MODE = 'A'
OPTIMISED_MODE = 'B'


def splitList(parentlist, refval):
    '''

    :param parentlist: List of objects
    :param refval: A number to identify break
    :return: List of lists, to hold groups of requests
    '''
    res = []
    startidx = 0
    i = 0
    while i < len(parentlist):
        if parentlist[i] == refval:
            endidx = i
            res.append(parentlist[startidx:endidx])
            startidx = i + 1
        i += 1
    res.append(parentlist[startidx:])
    return res


class Request():
    '''
    Class for a Request
    Start Floor, End Floor, Direction implied
    '''
    def __init__(self, start, end):
        self.start     = start
        self.end       = end
        self.direction = UP_SIGNAL if end > start else DN_SIGNAL

    def __str__(self):
        return '%d-%s-%d' % (self.start, self.direction, self.end)

    def getStart(self):
        return self.start

    def getDestination(self):
        return self.end

    def getDirection(self):
        return self.direction

    @staticmethod
    def mergeRequests(reqsList):
        '''
        Utility method, to merge Requests
        All requests in one DIRECTION, are merged into floors listing to be visited
        Floors will be in ascending order for UP move, viceversa

        :param reqsList: List or Request Objects
        :return: sorted Set, listing all the floors to be visited in sequential order
        '''

        overalldir = reqsList[0].getDirection()
        allFloors = []
        for i in range(len(reqsList)):
            allFloors.append(reqsList[i].getStart())
            allFloors.append(reqsList[i].getDestination())

        if overalldir == UP_SIGNAL:
            return sorted(set(allFloors))
        else:
            return sorted(set(allFloors), reverse=True)


class Elevator():
    '''
    Base class Elevator

    Resting on initfloor, at a given time working in dir Direction
    Queuing up requests in self.queue, processing via self.requests
    Travels through visitsequence, goes distance and comes to rest at initfloor again

    '''
    def __init__(self, initfloor, direction=None):
        self.dir       = direction
        self.initfloor = initfloor
        self.requests  = []
        self.distance  = 0
        self.queue     = []
        self.visitsequence = [initfloor]

    def getTraversedDistance(self):
        '''
        Traversed distance
        :return: total distance travelled by the Elev, int
        '''
        return self.distance

    def getVisitSequence(self):
        '''
        Sequence of floors visited
        :return: List of floor numbers
        '''
        return self.visitsequence

    def validateRequest(self, request):
        '''
        possible Validations for Requests
        :return: bool, can be implemented
        '''
        return True

    def addQueueRequest(self, request):
        '''
        Placeholder Queuing logic for LIFO requests
        :return: Throw on BASE
        '''
        raise NotImplementedError

    def serveRequests(self):
        '''
        Placeholder LIFO requests serving logic
        :return: Throw on BASE
        '''
        raise NotImplementedError


class SimpleElevator(Elevator):
    '''
    Simple Elevator

    no-logic queuing, just queue LIFO requests and send elevator on wild goose chase
    serve each request as it comes, also expend distance between requests
    '''

    def __init__(self, initfloor, direction=None):
        super().__init__(initfloor,direction)

    def addQueueRequest(self, request):
        '''

        :param request:
        :return: Modify Queue, add new requests one at a time
        '''
        if self.validateRequest(request):
            self.queue.append(request)

    def serveRequests(self):
        '''
        LOGIC :
        requests are collected, in the sequence they are input
        handle one request at a time
        increment the distance, record the floors visited
        '''
        if len(self.queue):
            self.requests.extend(self.queue)
            self.queue = []

        while len(self.requests):
            latestreq = self.requests.pop(0)
            start = latestreq.getStart()
            end   = latestreq.getDestination()

            # getting to and fro between requests
            if start != self.initfloor:
                self.dir = UP_SIGNAL if start > self.initfloor else DN_SIGNAL
                self.distance += abs(start - self.initfloor)
                self.visitsequence.append(start)

            # Start to end, on 1 request at a time
            self.dir       = latestreq.getDirection()
            self.initfloor = start
            self.distance += abs(start - end)
            self.initfloor = end
            self.visitsequence.append(end)


class OptimisedElevator(Elevator):
    '''
    OptimisedElevator

    queuing logic, to try bunch Same-Direction-Requests together
    convert such batch into sequence of floors

    Overall less floors halted, less distance
    '''

    def __init__(self, initfloor, direction=None):
        super().__init__(initfloor, direction)

    def addQueueRequest(self, request):
        '''

        :param request:
        :return: Modify Queue, add new requests one at a time
        '''
        if len(self.queue):
            prevreq = self.queue[-1]
            if prevreq.getDirection() is not request.getDirection():
                self.queue.append(TRIP_MARKER)

        self.queue.append(request)

    def serveRequests(self):
        '''
        LOGIC :
        use TRIP_MARKER to seperate bunch of same-directional requests
        merge these requests together, so elevator sees list of sorted floor #s
        traverse, increment the distance, record the floors visited
        '''

        initpos = self.initfloor

        reqssplit = splitList(self.queue, TRIP_MARKER)
        for reqlist in reqssplit:
            floors = Request.mergeRequests(reqlist)

            for floor in floors:
                self.distance += abs(floor - initpos)
                if self.visitsequence[-1] != floor:
                    self.visitsequence.append(floor)
                initpos = floor

def liftTypeFactory(mode=None):
    '''
    Factory entry point, to switch different implementations
    :param mode: Elevator Mode of operation
    :return: Implementation class
    '''
    typemapping = {
        SIMPLE_MODE: SimpleElevator,
        OPTIMISED_MODE: OptimisedElevator
    }

    if mode not in typemapping:
        raise KeyError("Mode %s not implemented, ensure you select these : %s" % (mode,','.join(typemapping.keys())))

    return typemapping[mode]


def handleRequests(inputstr, mode):
    '''

    :param inputstr: One line of requests. Format <InitFloor>:Start-End,Start-End,Start-End
    :param mode: Mode of elevator to be operated
    :return: print string, Flr1 Flr2 Flr3.. (Distance)
    '''
    initfloor, reqstr = inputstr.split(':')
    reqs = reqstr.split(',')

    reqobjs = []
    for r in reqs:
        s, e = r.split('-')
        reqobjs.append(Request(int(s), int(e)))

    elev = liftTypeFactory(mode)(int(initfloor))

    for req in reqobjs:
        elev.addQueueRequest(req)

    elev.serveRequests()
    l = elev.getVisitSequence()
    print('%s (%d)' % (' '.join(str(x) for x in l), elev.getTraversedDistance()))

# Entry point, read input file
def main(name='default-file.py', inputfile='G:\\Job\\Monticello\\input.txt', mode="A"):
    with open(inputfile) as f:
        lines = f.read().splitlines()
        for line in lines:
            handleRequests(line, mode)

main(*sys.argv)
