from lib.Server import Server
from lib.Protacol import Protacol

import pyautogui

class ControlServer(Server):
    def handle_request(self, request):
        self.logger('Handle request body:', request)

        try:
            if isinstance(request, list):
                respons = []
                for action in request:
                    respons.append(self.actions(action))
                return respons
            else:
                return self.actions(request)
        except:
            return {'status': False,
                    'message': 'handle_request error'}

    def actions(self, request):
        if(request['action'] == 'getsize'):
            return self.getSizeMonitor(request)

        if(request['action'] == 'moveto'):
            return self.moveTo(request)

        return {'status': False, 'message': 'no found method'}

    def getSizeMonitor(self, request):
        try:
            size = pyautogui.size()
            return {'status': True, 'message': '', 'size': size}
        except:
            return {'status': False, 'message': 'error getsize'}

    def moveTo(self, action):
        try:
            pyautogui.moveTo(action['x'],action['y'],action['time'])
            return {'status': True, 'message': ''}
        except:
            return {'status': False, 'message': 'error moveto'}

if __name__== '__main__':
    protacol = Protacol(10, lambda log: None)
    server = ControlServer(4002, protacol, print)
    server.run_server()
