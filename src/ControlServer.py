from lib.Server import Server
from lib.Protacol import Protacol

import pyautogui

class ControlServer(Server):
    def handle_request(self, request):
        self.logger(request)

        if(request['action'] == 'getsize'):
            return self.getSizeMonitor(request)

        if(request['action'] == 'moveto'):
            return self.getSizeMonitor(request)

        return {'status': False, 'message': 'no found method'} 

    def getSizeMonitor(self, request):
        try:
            size = pyautogui.size()
            return {'status': True,
                    'message': '',
                    'size': size}
        except:
            return {'status': False, 'message': ''}

    def moveTo(self, action):
        pyautogui.moveTo(action.x, action.y, action.time)

if __name__== '__main__':
    protacol = Protacol(10)
    server = ControlServer(4002, protacol, print)
    server.run_server()
