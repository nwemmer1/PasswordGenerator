from os import urandom
from random import choice

chars = { 'lowercase': 'abcdefghijklmnopqrstuvwxyz',
		  'uppdercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
		  'numbers': '0123456789',
		  'special': '!@#$%^&*()=+-_.,/?:;[]{}<>'
		}


def generate(length=21):
	
	password = []

	while len(password) < length:
		_key = choice(chars.keys())
		single_character = urandom(1)
		if single_character in chars[_key]:
			if prev_char(password, chars[_key]):
				continue
			else:
				password.append(single_character)
	return "".join(password)



def prev_char(_pass, curr_char):

	ind = len(_pass)
	if ind == 0:
		return False
	else:
		prev = _pass[ind - 1]
		if prev in curr_char:
			return True
		else:
			return False



if __name__ == '__main__':
	print generate()