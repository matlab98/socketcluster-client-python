import logging

from socketclusterclient import socketcluster


def on_connect(_socket):
    logging.info("on connect got called")


def on_disconnect(_socket):
    logging.info("on disconnect got called")


def on_connect_error(_socket, error):
    logging.error("On connect error got called")


def on_set_authentication(socket, token):
    logging.info("Token received " + token)
    socket.set_auth_token(token)


def on_authentication(_socket, is_authenticated):
    logging.info("Authenticated is " + str(is_authenticated))


if __name__ == "__main__":
    socket = socketcluster.Socket("ws://localhost:8000/socketcluster/")
    socket.set_basic_listener(on_connect, on_disconnect, on_connect_error)
    socket.set_authentication_listener(on_set_authentication, on_authentication)
    # socket.set_reconnection(False)
    socket.set_delay(2)
    socket.connect()
