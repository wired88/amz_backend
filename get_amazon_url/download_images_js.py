
import os
from tqdm import tqdm
import requests
from lxml import html
from urllib.parse import urljoin, urlparse

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    # make the HTTP request and retrieve response

    # Get the full html code

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
    }

    # request to server, response should be html code
    response = requests.get(url, headers=headers)
    print(f"Response: {response}\n")

    # convert in readeble format
    html_content = response.text
    print(f"html-content: {html_content}\n")

    # construct the parser
    tree = html.fromstring(html_content)
    urls = []

    # return the a Elements form the Page in a list
    anchor_tags = tree.xpath('//div[@data-component-type="s-search-result"]/div[@class="sg-col-inner"]/div/div/div/div/div/div/div/div/span/a')
    print(f"ist of figures: {anchor_tags}\n")
    for tag in anchor_tags:
        #get all anchor tags in figure
        anchors = tag.xpath('.//a[@class="_1n5grcph _1n5grcpk _1n5grcp4x0 _1n5grcp4yc _1n5grcp4zo _1n5grcp510 _1n5grcp1i _1n5grcp2i _1n5grcp36 _1n5grcpzo _1n5grcp3pi _1n5grcp3x0"]')
        print(f"Foubnd Product Links: {anchor_tags}\n")
        for anchor in anchors:
            #get link from that anchor to the image
            url_to_tag = anchor.get('href')
            if not url_to_tag:
                continue

            # Visit the Webpage
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 uacq'
            }
            response = requests.get(url_to_tag, headers=headers)
            html_content = response.text

            #get whole html of that new sitew
            tree_final_page = html.fromstring(html_content)



            #looking for the sitestripe window-hrefs
            all_img = tree_final_page.xpath('//img[@class="thumb"]')

            # loop through that list of img
            for img in all_img:
                #save here the src-attr-val ...
                img_class_final_url = (img.get('src') or
                                       img.get('data-src') or
                                       img.get('data-original'))
                if not img_class_final_url:
                    # if img does not contain src attribute, just skip
                    continue

                # and put the "base-link" in fron of it
                img_class_final_url = urljoin(url, img_class_final_url)

                #check fro validation and put them in the list of images
                if is_valid(img_class_final_url) and img_class_final_url not in urls:
                    urls.append(img_class_final_url)

    print("urls found: ", urls)
    return urls

def download(url, pathname):
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)

    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))

    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])

    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True,
                    unit_divisor=1024)

    try:
        with open(filename, "wb") as f:
            print("Downloading Data ...")
            for data in progress.iterable:
                # write data read to the file
                f.write(data)
                # update the progress bar manually
                progress.update(len(data))
    except:
        print(f"Download failed . . .")


def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each img, download it
        download(img, path)

search_params = [
    "iphone",
    "smartphone",
    "smartphone",
    "xbox",
    "playstation 5",
    "smartphone",
    "smartphone",
    "smartphone",
    "smartphone",
    "cyberpunk 2077",
    "Assassin's Creed Mirage",
    "Forza Motorsport 2023",
    "Der Herr der Ringe: Return to Moria",
    "Ghostrunner 2",
    "RoboCop: Rogue City ",
    "Call of Duty Modern Warfare 3 ",
    "Avatar - Frontiers of Pandora",
    "Crimson Desert",
    "Alan Wake 2",
]
"""
with open(os.path.join(f"{query}.txt"), "rw") as f:
    f.write(f"{link['description']}: {link['link']}\n")
    """
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="This script downloads all images from a web page")
    # parser.add_argument("url", help="https://example.art/")
    # parser.add_argument("-p", "--path",
    #        help="The Directory you want to store your images, default is the domain of URL passed")

    args = parser.parse_args()
    # url = args.url
    # path = args.path

    for key in search_params:
        print("Scanning Webpage for ", key, " . . .")
        main(f"https://www.amazon.de/s?k={key}",
             r"C:\Users\wired\OneDrive\Desktop\Scrapped\Picture\Everything")






"""
Problem:Solution
    - no figure-elements found: 

"""