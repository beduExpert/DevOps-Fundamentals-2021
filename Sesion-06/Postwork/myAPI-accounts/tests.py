import requests
import sys


def main():
    TestOK = True

    baseurl = f"http://{sys.argv[1]}:{sys.argv[2]}"

    print (f"Running for {baseurl}")

    print('Test 1 - Login with a non existant user')
    req = requests.get(f'{baseurl}/login?user=master&pass=race')
    if req.status_code != 401:
        TestOK = False
    if TestOK == False:
        print('Failed')
    else:
        print('Passed')

    print('Test 2 - Get account detail for non existant user')
    req = requests.get(f'{baseurl}/account?user=master')
    if req.status_code != 200:
        TestOK = False
    if req.text != '[]':
        TestOK = False
    if TestOK == False:
        print('Failed')
        sys.exit(1)
    else:
        print('Passed')
    
    print('Test 3 - Create user master')
    req = requests.post(f'{baseurl}/account?user=master&pass=race')
    if req.status_code != 200:
        TestOK = False
    if req.text != '{"msg": "Saved master"}':
        TestOK = False
    if TestOK == False:
        print('Failed')
        sys.exit(1)
    else:
        print('Passed')

    print('Test 4 - Delete user master')
    req = requests.delete(f'{baseurl}/account?user=master')
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