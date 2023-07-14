import sys
import re
import copy
from collections import defaultdict

def is_repeating(input_string):
    """Determine if the given input consists of two
    identical strings repeating after one another
    seperated by a whitespace.
    
    Args:
        input_string: any string
    
    Returns:
        boolean: true if input consists of repeating strings, false otherwise
        string: the string repeating itself if true, None otherwise
    """
    length = len(input_string)
    half_length = length // 2
    first_half = input_string[:half_length].strip()
    second_half = input_string[half_length + (length % 2):].strip()
    if first_half == second_half:
        return (True, first_half)
    else:
        return (False, None)
     
def find_target_product():
    """Finds the target product for the given file contents.
    
    Returns:
        string: target product
    """
    first_string = fc_split[0]
    while (" " + first_string + ",") not in file_contents:
        first_string = first_string.rsplit(' ', 1)[0]
    return first_string

def find_tp_index(target_product):
    """Finds the index of the target product 
    in fc_split (file contents delimited by commas).
    Used to find target product size, a number of
    input products, and a list of input products.
    
    Args:
        target_product
        
    Returns:
        integer: the index of target product in fc_split
    """
    tp_occurences = [i for i in fc_split if target_product in i] # all items in fc_split with tp as a substring
    for occurence in tp_occurences:
        if occurence.endswith(target_product):
            return fc_split.index(occurence)

def ip_size(target_product):
    """Finds the number of input products for a given 
    target product/product using a regular expression.
    
    Args:
        target_product
        
    Returns:
        integer: the number of input products
    """
    pattern = rf".*{re.escape(target_product)},([^,]+),([^,]+)"
    match = re.search(pattern, file_contents)
    if match:
        return int(match.group(2))

def price(target_product):
    """Finds the price for a given target 
    product/product using a regular expression.
    
    Args:
        target_product
        
    Returns:
        integer: the number of input products
    """
    pattern = rf".*{re.escape(target_product)},([^,]+),([^,]+)"
    match = re.search(pattern, file_contents)
    if match:
        if match.group(1) == "null":
            return "null"
        return float(match.group(1))

def find_ip(target_product):
    """Finds the input products of a target product
    
    Args:
        target_product
        
    Returns:
        list: input products
    """
    tp_index = find_tp_index(target_product)
    possible_ip = fc_split[tp_index + 3]
    possible_ip_list = possible_ip.split(";")
    ip_list = []
    
    for ip in possible_ip_list[:-1]:
        ip_list.append(ip)
    
    # remove word from last possible ip until it matches formatting
    last_ip = possible_ip_list[-1]
    while (" " + last_ip + ",") not in file_contents:
        last_ip = last_ip.rsplit(' ', 1)[0]
    ip_list.append(last_ip)      
            
    return [*set(ip_list)]

def find_cheapest_price(target_product):
    """Determines the cheapest price for a given target product/product.
    This function recursively finds the cheapest price between a given product
    and it's children. The base case is when a product has no input products.
    
    Args:
        target_product
        
    Returns:
        integer: the cheapest price between the product and it's input products
    """
    
    if ip_size(target_product) == 0:
        return round(price(target_product), 2)
    else:
        ips = find_ip(target_product)
        ip_price = 0
        for ip in ips:
            if price(ip) == "null" and ip_size(ip) == 0: # if the product can't be made or bought
                #ips_dict[target_product] += 1
                return price(target_product)
            ip_price += find_cheapest_price(ip)
        if price(target_product) != "null":
            #if price(target_product) <= ip_price: # product is cheaper to buy
                #ips_dict[target_product] += 1
            #else: # product is cheaper to make
                # for ip in ips:
                    #ips_dict[ip] += 1
            return min(price(target_product), ip_price)
        #ips_dict[ip] += 1 # if product can't be bought but can be made
        return round(ip_price, 2)
   
"""
def remove_more_expensive_ips(ips_dict):
    ips_dict_copy = copy.deepcopy(ips_dict)
    for product in ips_dict_copy:
        for ip in find_ip(product):
            ips_dict[ip] -= 1
    print(ips_dict)
    ret_list = []
    for product in ips_dict:
        ret_list.append(product)
    return ret_list
"""
    
with open(sys.argv[1], 'r') as f:
    file_contents = f.read()
    
fc_split = [s.strip() for s in file_contents.split(",")]
tp = find_target_product()
# ips_dict = defaultdict(int)
cheapest_price = find_cheapest_price(tp)
# ips_list = remove_more_expensive_ips(ips_dict)
#sys.stdout.write(str(ips_list))
#sys.stdout.write("\n")
sys.stdout.write(str(cheapest_price))