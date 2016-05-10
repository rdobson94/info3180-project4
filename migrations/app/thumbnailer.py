from bs4 import BeautifulSoup
import requests


def matching_words(string_1, string_2):
    count = 0
    string_1 = string_1.split()
    
    for word in string_1:
        if word in string_2:
            count += 1
    return count
    
def good_match(string, num_matching_words):
    string = string.split()
    str_len = len(string)
    if str_len > 0:
        percent =(float(num_matching_words)*100/float(str_len))
        if percent >= 50:
            return True
    return False

def get_data(url):
    try:
        result      = requests.get(url)
        soup        = BeautifulSoup(result.text, "html.parser")
        thumbnails  = []
        title       = ""
        
        if "amazon.com" in url:
            soup_title  = soup.find("span",id="productTitle")
            soup_img    = soup.find_all("img", id="landingImage")
            
            if not soup_img:
                return {"error":1,"data":{},"message":"Unable to extract images."}
            else:
                for img in soup_img:
                    if img["src"] not in thumbnails:
                        thumbnails.append(img["src"])
                
                if soup_title:
                    title = soup_title.string

            return {"error":None,"data":{"title":title, "thumbnails":thumbnails},"message":"Success"}
        
        elif "ebay.com" in url:
            soup_title = soup.find("h1", id="itemTitle")
            soup_img = soup.find_all("img", id="icImg")
            
            if not soup_img:
                return {"error":1,"data":{},"message":"Unable to extract images."}
            else:
                for img in soup_img:
                    if img["src"] not in thumbnails:
                        thumbnails.append(img["src"])
                
                if soup_title:
                    children = []
                    for child in soup_title.children:
                        children.append(child)
                    title = children[1]

            return {"error":None,"data":{"title":title, "thumbnails":thumbnails},"message":"Success"}
        
        else:
            title = soup.title.string
            for img in soup.find_all("img", alt=True):
                alt = img['alt']
                src = img['src']
                numMatchingWords = matching_words(title,alt)
                if good_match(alt, numMatchingWords):
                    if src not in thumbnails and src[-4:]==".jpg" and "sprite" not in src:
                        thumbnails.append(src)
            
            if not thumbnails:
                for img in soup.findAll("img", src=True):
                    if "sprite" not in img["src"] and src[-4:]==".jpg":
                        thumbnails.append(img["src"])
            
            if not thumbnails:
                return {"error":1,"data":{},"message":"Unable to extract images."}
    
            return {"error":None,"data":{"title":title, "thumbnails":thumbnails},"message":"Success"}
    
    except requests.exceptions.RequestException:
        return {"error":2,"data":{},"message":"URL entered is invalid."}
    
    

url1 = "http://www.ebay.com/itm/ROLEX-Day-Date-II-Presidential-w-Factory-Diamond-Bezel-Dial-218348-/172103028001?hash=item281223cd21:g:gRcAAOSwezVWwhkv"
url2 = "http://intl.target.com/p/mr-coffee-cafe-barista-bvmc-ecmp1000/-/A-14575718#prodSlot=_1_8"
url3 = "http://www.amazon.com/gp/product/B00THKEKEQ/ref=s9_ri_gw_g421_i1_r?ie=UTF8&fpl=fresh&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-4&pf_rd_r=1WEK74K6Y8MXQC6BSHDN&pf_rd_t=36701&pf_rd_p=2437869562&pf_rd_i=desktop"
url4 = "http://www.amazon.com/gp/product/B012GC5DX8/ref=s9_qpp_gw_d38_g107_i1_r?ie=UTF8&fpl=fresh&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-1&pf_rd_r=0HX3HCEVK96HB5FDXMV0&pf_rd_t=36701&pf_rd_p=2437869742&pf_rd_i=desktop"
url5 = "http://www.ebay.com/itm/Lamborghini-Aventador-LP-750-4-SV-/231914556159?forcerrptr=true&hash=item35ff2f4aff:g:4ckAAOSwiYFXESqj&item=231914556159"
url6 = "http://www.amazon.com/Hifonics-ZRX2416-1D-Block-Vehicle-Amplifier/dp/B00T3VMTPQ?ie=UTF8&refRID=PX2YE82MNZZBNBDCRWSS&ref_=pd_ybh_a_1"
url7 = "http://www.amazon.com/Power-Acoustik-GW312-1200WATT-2500WATT/dp/B00B7C077G?ie=UTF8&psc=1&redirect=true&ref_=ox_sc_sfl_title_5&smid=A35DL6C7BAXYRR"
url8 = "http://www.ebay.com/itm/Apple-12-MacBook-Intel-Core-M-1-1GHz-8GB-RAM-256GB-Flash-Early-2015-Gold/262417285736?hash=item3d194a0268&_trkparms=5374%3AFeatured%7C5373%3A0"


#print get_data(url1)
#print get_data(url2)
#print get_data(url3)
#print get_data(url4)
#print get_data(url5)
#print get_data(url6)
#print get_data(url7)
#print get_data(url8)