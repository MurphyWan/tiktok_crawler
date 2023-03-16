import requests
import json

# 用于获取TikTok API的访问令牌
def get_access_token():
    # 用于获取访问令牌的URL
    url = 'https://api.tiktok.com/oauth/access_token/'
    # 设置请求参数
    data = {
        'app_id': '你的应用程序ID',
        'app_secret': '你的应用程序密钥',
        'grant_type': 'client_credential'
    }
    # 发送请求
    response = requests.post(url, data=data)
    # 解析响应
    access_token = json.loads(response.text)['access_token']
    return access_token

# 获取直播数据
def get_live_data(user_id, access_token):
    # 用于获取直播数据的URL
    url = f'https://api.tiktok.com/lives/v2/user/{user_id}/info/'
    # 设置请求参数
    params = {
        'access_token': access_token
    }
    # 发送请求
    response = requests.get(url, params=params)
    # 解析响应
    data = json.loads(response.text)['data']
    # 输出结果
    print(f"用户名: {data['nickname']}")
    print(f"直播间标题: {data['title']}")
    print(f"观看人数: {data['viewer_count']}")

if __name__ == '__main__':
    # 获取访问令牌
    access_token = get_access_token()
    # 设置要获取直播数据的用户ID
    user_id = '用户ID'
    # 获取直播数据
    get_live_data(user_id, access_token)
