import socket

def main():
    # create an udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        #msg = 'hello'
        msg =input('输入消息:\n') 
        if msg == 'exit':
            break
        print('send msg :'+msg)
        #udp_socket.sendto(b'hello', ('192.168.31.32', 8080))
        udp_socket.sendto(msg.encode('utf-8'), ('192.168.31.32', 8080))

    udp_socket.close()



if __name__ == "__main__":
    main()
