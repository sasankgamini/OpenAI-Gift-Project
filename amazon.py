import boto3
import urllib.parse

# Set up AWS credentials and region
AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
AWS_ASSOCIATE_TAG = 'your-associate-tag'
AWS_REGION = 'us-east-1'

# Initialize the Product Advertising API client
client = boto3.client('s3',
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                      region_name=AWS_REGION)

def get_affiliate_link(product):
    # Search for the product using the ItemSearch operation
    response = client.ItemSearch(
        SearchIndex='All',
        Keywords=product,
        ResponseGroup='ItemIds'
    )

    # Get the ASIN of the first product in the search results
    asin = response['Items'][0]['Item'][0]['ASIN']

    # Construct the affiliate link with your associate tag
    url = f'https://www.amazon.com/dp/{asin}/?tag={AWS_ASSOCIATE_TAG}'

    # Encode the link to handle special characters
    return urllib.parse.quote(url, safe=':/')

# Example usage
product = input("Enter a product: ")
link = get_affiliate_link(product)
print(f"Affiliate link for {product}: {link}")
