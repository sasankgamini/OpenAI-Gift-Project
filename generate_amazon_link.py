import urllib.parse

def generate_amazon_link(product_name):
    base_url = 'https://www.amazon.com/s?'
    query_params = {
        'k': product_name,
        'ref': 'nb_sb_noss'
    }
    encoded_params = urllib.parse.urlencode(query_params)
    return base_url + encoded_params

# Example usage
if __name__ == "__main__":
    product_name = input('Enter a product name: ')
    amazon_link = generate_amazon_link(product_name)
    print('Amazon link:', amazon_link)