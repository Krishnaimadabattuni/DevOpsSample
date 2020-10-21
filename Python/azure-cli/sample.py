import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.network.v2017_03_01.models import NetworkSecurityGroup
from azure.mgmt.network.v2017_03_01.models import SecurityRule

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '7c2437d7-ad24-4195-b9b9-08b22f8cca17') # your Azure Subscription Id
credentials = ServicePrincipalCredentials(
    client_id='30cefe76-bcbb-4bdc-ba02-749dfeb459c2',
    secret='rVbww2Ge8G~RZvb_pvUGTVrXUs1neC_7-I',
    tenant='dc852cab-92fb-44c9-8aeb-f3b3bc3584e1'
)
resource_client = ResourceManagementClient(credentials, subscription_id)
network_client = NetworkManagementClient(credentials,subscription_id)
GROUP_NAME = input("Please Enter ResourceGroupName: ")
GROUP_LOCATION = input("Please Enter GroupLocation: ")

def resourcegroup():               
    if len(GROUP_NAME) > 0 and len(GROUP_LOCATION) > 0: 
        print("Creating resource group...........") 
        resource_client.resource_groups.create_or_update(GROUP_NAME,{"location": GROUP_LOCATION})                     
    else:
        print("unable to create Resource Group........")
        
resourcegroup() 

############################
#-------------Virtual Networks###############
def virtualnetwork():      
    VNET_NAME = input("Please Enter a Virtual Network Name: ") 
    if len(VNET_NAME) > 0:
        print("Creating Virtual Network....")
        network_client.virtual_networks.create_or_update(GROUP_NAME,VNET_NAME,{'location':GROUP_LOCATION,'address_space': {'address_prefixes': ['10.0.0.0/16']}})
    else:
        print("unable to create the virtual network...")    
    SUBNET_NAME= input("Please Enter a Subnet Name: ")
    if len(VNET_NAME) > 0 and len(SUBNET_NAME) > 0: 
        print("creating the subnet...........")  
        network_client.subnets.create_or_update(GROUP_NAME,VNET_NAME,SUBNET_NAME,{'address_prefix': '10.0.0.0/24'})
    else:
        print("Failed to create the subnet..............")
virtualnetwork()

##########################
#-------------NSG Rules###############

print("testing............")

resource_group_name = GROUP_NAME

network_security_group_name =GROUP_NAME + '-NSG'

security_rule = SecurityRule( protocol='Tcp', source_address_prefix='*', 
                              source_port_range="*", destination_port_range="*", priority=100,
                              destination_address_prefix='*', access='Allow', direction='Inbound')
nsg_params = NetworkSecurityGroup(id=network_security_group_name, location=GROUP_LOCATION, tags={ 'name' : 'testnsg' })
network_client.network_security_groups.create_or_update(resource_group_name,network_security_group_name, parameters=nsg_params, security_rules=[security_rule])

