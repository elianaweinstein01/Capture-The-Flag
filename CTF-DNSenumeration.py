from scapy.all import *
import sys
#Eliana Weinstein
#34718223

#queries the start of authority record for a
#specified domain to determine primary name server
#return: name of dns server
def soa_dns_server(domain):
    #Create an SOA DNS query packet to recieve a response
    #(i originally used goodles (8.8.8.8) and thats how i got the word list)
    #i switched it to 1.1.1.1, some of the ip addresses are different and some
    #subdomains dont come up
    dns_query = IP(dst="1.1.1.1") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain, qtype='SOA'))

    print("Sending SOA DNS query packet")
    #Sending the SOA DNS query and then receive the response
    dns_response = sr1(dns_query, verbose=0)

    #Check if we received a response and checking if it contains the expected layers. We need to check this
    #to be make sure that the computer can process it correctly
    if dns_response and dns_response.haslayer(DNS):
        #saves the current layer of the dns packet so we can work directly with the layer being sent by scapy
        layer = dns_response.getlayer(DNS)
        #ancount = answercount. checking if the dns response contains any answer records
        if layer.ancount > 0:
            #accesses the answer section of the dns response. record acesses the first answer.
            record = layer.an[0]
            #gets the primary name of the server from the answer section
            name_server = record.mname.decode('utf-8')
            #print the primary name server.
            print(f"Primary Name Server: {name_server}")
            return name_server
        #if there are no answer records, an soa record is not found
        else:
            print(f"No SOA record found for {domain}")
    #no response received from the query
    else:
        print("No response received.")
    return None

#input is domain, the soa response of dns server, list of wors
#function creates dns query for each subdomain in wordlist
#and checks if it exists and if so what its ip addresses are.
#prints all subdomains with their ip addresses.
def dns_enum(domain, name_server, wordlist):

    # opens specified file in read mode. closes file after reading.
    with open(wordlist, 'r') as file:
        # splits the whole string into a list of lines and returns a list of the lines. each line
        # in file becomes an element of the list
        # list of all the words in the wordList
        subdomains = file.read().splitlines()

    #for each word in the subdomains list.
    for sub in subdomains:
        #concatinates the subdomain with the input domain.
        domain_name = f"{sub}.{domain}"
        #creates a dns query packet using scapy. sets the server IP address, port 53(standard dns queries port)
        #dns creates a layer for the query, specifies the domain name (recived from word list)
        dns_query = IP(dst=name_server) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=domain_name, qtype='A'))

        #sends it and recives response to dns_query
        dns_response = sr1(dns_query, verbose=0, timeout=2)

        #checks if response recived and has proper layers
        if dns_response and dns_response.haslayer(DNS):
            #sets layer to be the layer of the response
            layer = dns_response.getlayer(DNS)
            #if layer has answer section
            if layer.ancount > 0:
                #create array with all the full addresses
                full_addresses = []
                #iterates over the answer records
                for i in range(layer.ancount):
                    answer = layer.an[i]
                    # ensure it is an a record containing an ipv4 address.
                    if answer.type == 1:
                        #adds the actual ip address to list
                        full_addresses.append(answer.rdata)
                #if the list is not empty
                if full_addresses:
                    #print out the domain name, with all of its ip adresses found, with a comma in between.
                    print(f"{domain_name} - {', '.join(full_addresses)}")


if __name__ == "__main__":
    #ensures that the correct number of command line inputs. (the script name, the domain, and the wordlist file.
    if len(sys.argv) != 3:
        #prints a message to specify to user what input is.
        print("Usage: python dnsenum.py <domain> <wordlist>")
    else:
        #domain is set to second input from user
        domain = sys.argv[1]
        #wordList is set to third input from user
        wordlist = sys.argv[2]
        #name of server is set to soa dns server
        name_server = soa_dns_server(domain)

        #if dns server name exists:
        if name_server:
            dns_enum(domain, name_server, wordlist)

"""
**input**
(.venv) elianaweinstein@Elianas-MacBook-Air lab4 % python3 DNSenumeration.py google.com secret_subdomains.txt

Output:

WARNING: No IPv4 address found on anpi0 !
WARNING: No IPv4 address found on anpi1 !
WARNING: more No IPv4 address found on en3 !
Sending SOA DNS query packet
Primary Name Server: ns1.google.com.
amp.google.com - 142.250.75.78
api.google.com - 142.250.75.68
web.google.com - 142.250.75.78
download.google.com - 142.250.75.68
mail.google.com - 142.251.37.69
ns3.google.com - 216.239.36.10
support.google.com - 142.251.37.78

"""


