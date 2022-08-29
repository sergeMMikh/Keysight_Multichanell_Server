from cls_SocketServer import SocketServer
from cls_instrument import DeviceM


def main():
    server = SocketServer()
    device_m = DeviceM('instr_idn.txt')
    print(device_m.open_instrument())

    while True:
        recvData = server.recv_server_data().decode().strip()
        match recvData:
            case 'Exit':
                server.send_str_server_data('Close multimeter program.')
                server.close()
                break
            case 'Idn' | 'IDN' | 'idn':
                server.send_str_server_data(device_m.idn)
            case 'Meas' | 'MEAS' | 'meas':
                server.send_str_server_data(device_m.make_meas())
            case 'Error' | 'ERROR' | 'error'| 'Errors' | 'ERRORS' | 'errors':
                server.send_str_server_data(device_m.get_errors())
            case _:
                server.send_str_server_data(f'Unknown command: {recvData}')


if __name__ == "__main__":
    main()
