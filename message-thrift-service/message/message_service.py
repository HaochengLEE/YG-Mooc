from message.api import MessageService
from thrift.transport import TSocket

class MessageServiceHandler:

    def sendMpbileMessage(self,moblie,message):
        print "sendMobileMessage"
        return True

    def sendEmailMessage(self,email,message):
        print "sendEmailMessage"
        return True


if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.


