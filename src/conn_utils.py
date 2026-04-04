import socket

def is_online():
    try:
        #"Ping" Google
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        try:
            # "Ping" Cloudflare
            socket.create_connection(("1.1.1.1", 53), timeout=2)
            return True
        except:
            try:
                # "Ping" Quad9
                socket.create_connection(("9.9.9.9", 53), timeout=2)
                return True
            except:
                return False
