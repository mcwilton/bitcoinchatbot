from blockcypher import get_address_overview
import requests

def check_balancer(address):
	reply= requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance')
	to_json= reply.json()
	#print(to_json['final_balance'])
	return to_json['final_balance']

check_balance = 'qr code 1M5m1DuGw4Wyq1Nf8sfoKRM6uA4oREzpCX'

address1 = check_balance.split()[2]

final = check_balancer(address1)
print(final)



# check balance 1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD
elif 'check balance' in incoming_msg:
	address = incoming_msg[2]
	final = check_balance(address)
	msg.body(f"Your address has a balance of {final}")
	responded = True




#add = get_address_overview(address1)

#print(add['final_balance'])
#



def check_balance(address):
	add = get_address_overview(address)
	return add['address']


def check_balancer(address):
	reply= requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance')
	to_json = reply.json()
	return to_json['final_balance']

