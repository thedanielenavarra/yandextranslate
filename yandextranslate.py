import requests
import argparse
import json

def ydx(args):
	url="https://translate.yandex.net/api/v1.5/tr.json/translate"
	pld={"lang": args.l1+"-"+args.l2, "text": args.text, "key": "trnsl.1.1.20190902T140049Z.b445ec296d81e8b2.e41fa3eb97f4aebb7e7074fd561b0faef1846592"}
	r=requests.get(url, params=pld)
	return json.loads(r.text)


def main():
	ap=argparse.ArgumentParser(prog="Yandex Translate")
	ap.add_argument("--from", help="Translate from language", dest="l1")
	ap.add_argument("--to", help="Translate to language", dest="l2")
	ap.add_argument("--text", help="Translate text", dest="text")
	
	args=ap.parse_args()

	return ydx(args)

#print(main())
