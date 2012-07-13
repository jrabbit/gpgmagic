import subprocess

def sign(email, message):
    return subprocess.check_output(['gpg', '-u', email, '-a', '--output', '-', '--clearsign', '-' ], stdin=message)