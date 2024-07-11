import requests

url = 'https://gorest.co.in/public/v2/users'
headers = {"Accept": "application/json",
           "Content-Type": "application/json",
           "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"
           }


# response = requests.get(url, headers=headers)
# print(response)
# print(response.status_code)
# print(type(response.text))
# print(response.json()[0])
# print(response.content)
# print(response.cookies)
# print(response.headers)



# response = requests.get('http://google.com', headers=headers)
# #print(response.json())
# #print(response.text)
# coockies = response.cookies
# print(response.cookies)


# #url = 'https://gorest.co.in/public/v2/users?gender=male&id=7018136'
# url = 'https://gorest.co.in/public/v2/users'
# #gender=male&id=7018136
# #params = {'gender': 'male', 'id': '7018136'}
# params = [('gender', 'male'), ('id', '7018136')]
#
# response = requests.get(url, headers=headers, params=params)
# print(response.status_code)
# print(response.json())

url = 'https://gorest.co.in/public/v2/users'
# body = {"name":"User11111111", "gender":"male", "email":"user1@15ce.com", "status":"active"}
# response = requests.post(url, json=body, headers=headers)
# print(response.status_code)
# print(response.json())

# 7024540
# params = {"name": "User11111111"}
# response = requests.get(url, headers=headers, params=params)
# print(response.json())

# response_put = requests.patch(f"https://gorest.co.in/public/v2/users/7024540", data='{"status":"active"}', headers=headers)
# print(response_put.status_code)
# print(response_put.json())


# headers_delete = {"Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"
#            }
#
# # response_delete = requests.delete(f"https://gorest.co.in/public/v2/users/7024540", headers=headers_delete)
# # print(response_delete.status_code)
# # print(response_delete.json())
#
# params = {"name": "User11111111"}
# response = requests.get(url, headers=headers, params=params)
# print(response.json())





######################################################################################################################
# # Options
header_for_options = {"Accept": "application/json",
                      "Content-Type": "application/json",
                      "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c",
                      'Access-Control-Request-Method': 'DELETE',
                      'Access-Control-Request-Headers': 'origin, x-requested-with',
                      'Origin': 'https://gorest.co.in'
                      }

url = 'https://gorest.co.in/public/v2/users'
response = requests.options(url, headers=header_for_options)
print(response)
print(response.status_code)
print(response.text)
print(response.headers)
print(response.headers.get('access-control-allow-methods', 'No info:('))