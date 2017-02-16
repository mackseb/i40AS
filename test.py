from structure import configuration_shell

abc = 'database'

if configuration_shell.data.get(abc, False):
    print('request exists')
else:
    print('no match')
