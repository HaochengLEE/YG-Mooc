namespace java com.mooc.thrift.message
namespace py message.api


service MessageService{
    bool sendMoblieMessage(1:string moblie,2:string message);

    bool sendEmailMessage(1:string email,2:string message);




}