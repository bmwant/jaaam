"""
Example of one-time password validation
"""
import json
import sys
import os
import signal


USER_ID = 2
CODE_FILENAME = "code"
REQUEST_FILENAME = "request"


def send_authorize_request(pid: int):
    # Obtain OTP code
    with open(CODE_FILENAME) as f:
        code = f.read()

    # Prepare payload
    payload = {
        "user_id": USER_ID,
        "code": code,
    }
    with open(REQUEST_FILENAME, "w") as f:
        f.write(json.dumps(payload))

    # Send request
    print(f"Sending request with a code {code}...")
    os.kill(pid, signal.SIGUSR1)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        raise RuntimeError("Wrong usage, provide server PID")
    
    send_authorize_request(int(sys.argv[1]))