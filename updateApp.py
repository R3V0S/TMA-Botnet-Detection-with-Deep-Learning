def cleanDf(df):
	pmap = {'1': 2, '6': 11} # Are 1 or 6 strings or ints?
	df['Proto'] = df['Proto'].map(pmap)
	
def checkBots(df):
	predictions = model.predict(df)
    
    if(predictions == ???): # output of the model to check if we received an attack
        list_ddos_attackers = [] # List to append the attackers ip
        ips = df['ipv4-src'].unique()) # List of different ips in source column
        for ip in ips: # iterate over the ips list
            myobj = {'nw_src': ip + '/32', 'actions': 'DENY', 'dl_type': 'IPv4', 'priority': '10'}
            x = requests.post(urlFirewall, json=myobj) # urlFirewall correct value in declaration?
            list_ddos_attackers.append(ip)
            
        print('ATTACKERS BANNED')
        
def detectBots():
    client = connectDB()
    segment = 0
    num_flows = 80
    while True:
        df = query(client, segment, segment + num_flows)
        cleanDf(df)
        checkBots(df)
        sleep(2)
        #Missing condition to increment segment
        if():
            segment += 40
        
if __name__ == '__main__':

    detectBots()