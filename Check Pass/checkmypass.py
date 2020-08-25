import requests
import hashlib
import sys

def request_api_data(query_char):
    '''
    Function that receive the first 5 sha1 chars and send it to an api to check the breaches in a series of coincidental passwords
    :param query_char: string with first 5 sha1 chars
    :return: Response from the api, base with tails and count
    '''
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code!= 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
    return res

def get_password_leaks_counts(hashes, hash_to_check):
    '''
    Function that separate the response and review
    :param hashes: text response from the api
    :param hash_to_check: tail to review
    :return: the number of times that the password has been breached
    '''
    hash = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hash:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    '''
    Function that codify a password on sha1, separate de first 5 chars and use the request_api_data() to receive a response
    :param password: String
    :return: response test and tail of the codify hash
    '''
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #utf-8, encode to b'password'
    first5_char, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_counts(response, tail) # devuelve los hash

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'The password {password} has been breached {count} times')
        else:
            print(f'The password {password} was not found')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

