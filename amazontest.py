# import boto3
# import urllib.parse

# # Set up AWS credentials and region
# AWS_ACCESS_KEY_ID = 'your-access-key-id'
# AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
# AWS_ASSOCIATE_TAG = 'your-associate-tag'
# AWS_REGION = 'us-east-1'

# # Initialize the Product Advertising API client
# client = boto3.client('s3',
#                       aws_access_key_id=AWS_ACCESS_KEY_ID,
#                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#                       region_name=AWS_REGION)

# def get_affiliate_link(product):
#     # Search for the product using the ItemSearch operation
#     response = client.ItemSearch(
#         SearchIndex='All',
#         Keywords=product,
#         ResponseGroup='ItemIds'
#     )

#     # Get the ASIN of the first product in the search results
#     asin = response['Items'][0]['Item'][0]['ASIN']

#     # Construct the affiliate link with your associate tag
#     url = f'https://www.amazon.com/dp/{asin}/?tag={AWS_ASSOCIATE_TAG}'

#     # Encode the link to handle special characters
#     return urllib.parse.quote(url, safe=':/')

# # Example usage
# product = input("Enter a product: ")
# link = get_affiliate_link(product)
# print(f"Affiliate link for {product}: {link}")










# import requests
# from bs4 import BeautifulSoup

# def generate_amazon_link(product_name):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
#     }
#     search_url = f'https://www.amazon.com/s?k={product_name}&ref=nb_sb_noss'
#     response = requests.get(search_url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     results = soup.find_all('div', {'data-component-type': 's-search-result'})
#     if results:
#         for result in results:
#             product_title = result.find('h2', {'class': 'a-size-mini'}).text.strip()
#             if product_name.lower() in product_title.lower():
#                 product_url = result.find('a', {'class': 'a-link-normal'})['href']
#                 return product_url
#         return None
#     else:
#         return None

# # Example usage
# product_name = input('Enter a product name: ')
# amazon_link = generate_amazon_link(product_name)
# if amazon_link:
#     print('Amazon link:', amazon_link)
# else:
#     print('No products found on Amazon for', product_name)



