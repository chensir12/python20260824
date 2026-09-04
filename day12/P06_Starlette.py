"""
    该案例演示了通过starlette开发web服务
"""
import requests
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

# 一言网的 API 地址
HITOKOTO_URL = 'https://v1.hitokoto.cn/'

# 定义异步函数来获取随机名言
async def get_hitokoto():
    try:
        # 请求参数，指定返回中文内容，这里使用默认的所有类型
        params = {
            'c': 'a',  # 可以根据需要修改类型，a 代表动画，b 代表漫画等
            'encode': 'json'
        }
        response = requests.get(HITOKOTO_URL, params=params)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            hitokoto = data['hitokoto']
            from_who = data['from_who'] if data['from_who'] else '未知'
            return {'hitokoto': hitokoto, 'from_who': from_who}
        else:
            return {'error': f'请求一言网 API 失败，状态码: {status_code}'}
    except requests.RequestException as e:
        return {'error': f'请求过程中出现错误: {str(e)}'}

# 定义处理根路径请求的异步函数
async def homepage(request):
    result = await get_hitokoto()
    return JSONResponse(result)

# 创建 Starlette 应用实例
app = Starlette(debug=True, routes=[
    Route('/', homepage),
])

if __name__ == '__main__':
    # 使用uvicorn 运行应用
    uvicorn.run(app, host='0.0.0.0',port=8000)