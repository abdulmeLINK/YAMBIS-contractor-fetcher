import json
import requests
import datetime
import argparse
# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="YAMBIS contractor fetcher")

# Add optional arguments
parser.add_argument("-l", "--length", type=int, default=10,
                    help="Length of incoming data")
parser.add_argument("-p", "--pcode", type=int,
                    help="Province code for example 34 will get only contractors in İstanbul")
parser.add_argument("-s", "--startAt", type=int, default=0,
                    help="Fetching start index")
parser.add_argument("--sessionId", type=str,
                    help="ASP.NET_SessionId", required=True)
# Parse the command-line arguments
args = parser.parse_args()
# Define the URL and data to be sent in the request
url = "https://yambis.csb.gov.tr/Muteahhit/getMuteahhitKisilerJSON"
# Set default values for optional arguments
maxlen = 4000
data_length = args.length
pcode = args.pcode or ""
startAt = args.startAt

loop_count = (data_length // maxlen)
if data_length % maxlen != 0:
    loop_count += 1
for i in range(loop_count):
    if i > 0:
        startAt += (maxlen * i) + 1

    current_length = data_length
    if data_length >= maxlen:
        current_length = maxlen

    data = f"""draw=2&columns%5B0%5D%5Bdata%5D=KisiId&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=VergiNo&columns%5B1%5D%5Bname%5D=VergiNo&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=TcNo&columns%5B2%5D%5Bname%5D=TcNo&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=Ad&columns%5B3%5D%5Bname%5D=Ad&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=Soyad&columns%5B4%5D%5Bname%5D=Soyad&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=Tanim&columns%5B5%5D%5Bname%5D=Tanim&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=KisiTuru&columns%5B6%5D%5Bname%5D=KisiTuru&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=Il&columns%5B7%5D%5Bname%5D=Il&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=GeciciMi&columns%5B8%5D%5Bname%5D=GeciciMi2&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=ElektronikHaberlesmeMuteahhitiMi&columns%5B9%5D%5Bname%5D=ElektronikHaberlesmeMuteahhitiMi&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=YetkiBelgeNo&columns%5B10%5D%5Bname%5D=YetkiBelgeNo&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=true&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=Durum&columns%5B11%5D%5Bname%5D=Durum&columns%5B11%5D%5Bsearchable%5D=true&columns%5B11%5D%5Borderable%5D=true&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B12%5D%5Bdata%5D=YasaklamaNedeni&columns%5B12%5D%5Bname%5D=YasaklamaNedeni&columns%5B12%5D%5Bsearchable%5D=true&columns%5B12%5D%5Borderable%5D=true&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=YapimMuteahhitiMi&columns%5B13%5D%5Bname%5D=YapimM%C3%BCteahhitiMi&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=true&columns%5B13%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D=KararGrupTipi&columns%5B14%5D%5Bname%5D=KararGrupTipi&columns%5B14%5D%5Bsearchable%5D=true&columns%5B14%5D%5Borderable%5D=true&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B15%5D%5Bdata%5D=YikimMuteahhitiMi&columns%5B15%5D%5Bname%5D=YikimMuteahhitiMi&columns%5B15%5D%5Bsearchable%5D=true&columns%5B15%5D%5Borderable%5D=true&columns%5B15%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B15%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B16%5D%5Bdata%5D=YikimKararGrupTipi&columns%5B16%5D%5Bname%5D=YikimKararGrupTipi&columns%5B16%5D%5Bsearchable%5D=true&columns%5B16%5D%5Borderable%5D=true&columns%5B16%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B16%5D%5Bsearch%5D%5Bregex%5D=false&start={startAt}&length={current_length}&search%5Bvalue%5D=&search%5Bregex%5D=false&action=filter&VergiNo=&TcNo=&Ad=&Soyad=&Tanim=&KisiTuruId=-1&IlKodu={pcode}&GeciciMi2=-1&ElektronikHaberlesmeMuteahhitiMi=-1&YetkiBelgeNo=&DurumId=-1"""

    # Encode the data as form-urlencoded
    encoded_data = data

    # Define the headers for the request
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": f"ASP.NET_SessionId={args.sessionId}",
        "Host": "yambis.csb.gov.tr",
        "Origin": "https://yambis.csb.gov.tr",
        "Referer": "https://yambis.csb.gov.tr/Muteahhit/Index",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
    }

    # Send the POST request with headers and encoded data
    response = requests.post(url, data=encoded_data, headers=headers)
    print(response.text)
    # Check if the request was successful (status code 200)
    data_length -= current_length
    if response.status_code == 200:
        # Load the response JSON data
        response_data = response.json()
        x = datetime.datetime.now().timestamp()
        if pcode == "":
            file_name = f"output/unfiltered/contractors_startsat{startAt}_len{current_length}_{x}.json"
        else:
            file_name = f"output/filtered/contractors_{pcode}_startsat{startAt}_len{current_length}_{x}.json"
        # Save the response data as a JSON file
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=4)
            print("Response data saved")
    else:
        print("Failed to send POST request. Status code:", response.status_code)
        exit()
