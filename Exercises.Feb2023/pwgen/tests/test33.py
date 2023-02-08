from pwgen import genpw

x = len(genpw.pass_gen('medium'))
if x >= 12 and x <= 17:
    print('true')


