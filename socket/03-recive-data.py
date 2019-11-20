import socket

def main():
    # create an udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    localAddr = ('',7788)
    udp_socket.bind(localAddr)
    while True:
        # 接受数据
        recv_data = udp_socket.recvfrom(1024)
        msg = recv_data[0]
        address = recv_data[1]
        print('%s:%s' % (str(address),msg.decode('gbk')))
    udp_socket.close()



if __name__ == "__main__":
    main()
