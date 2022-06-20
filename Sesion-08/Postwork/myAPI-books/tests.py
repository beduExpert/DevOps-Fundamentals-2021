import requests
import json
import sys


def main():
    TestOK = True

    baseurl = f"http://{sys.argv[1]}:{sys.argv[2]}"

    print (f"Running for {baseurl}")

    print('Test 1 - Get a non existant book')
    req = requests.get(f'{baseurl}/book?isbn=0618346252')
    if req.status_code != 200:
        TestOK = False
    if req.text != '[]':
        TestOK = False
    if TestOK == False:
        print('Failed')
        sys.exit(1)
    else:
        print('Passed')

    print('Test 2 - Add a book')
    req = requests.post(f'{baseurl}/book?isbn=0618346252&title=The Fellowship of the Ring')
    if req.status_code != 200:
        TestOK = False
    if req.text != '{"msg": "Saved 0618346252"}':
        TestOK = False
    if TestOK == False:
        print('Failed')
        sys.exit(1)
    else:
        print('Passed')

    print('Test 3 - Get book by ISBN')
    TestOK = False
    req = requests.get(f'{baseurl}/book?isbn=0618346252')
    if req.status_code == 200:
        robj = json.loads(req.text)
        if robj[0]['isdn'] == "0618346252" and robj[0]['title'] == "The Fellowship of the Ring":
            TestOK = True
    if TestOK == False:
        print('Failed')
        sys.exit(1)
    else:
        print('Passed')

    print('Test 4 - Delete a book')
    req = requests.delete(f'{baseurl}/book?isbn=0618346252')
    if req.status_code != 200:
        TestOK = False
    if req.text != '{"msg": "Deleted", "count": "1"}':
        TestOK = False
    if TestOK == False:
        print('Failed')
        sys.exit(1)
    else:
        print('Passed')


    print('All tests passed')
    sys.exit(0)

if __name__ == "__main__":
    main()