import pytest

@pytest.fixture(scope='module')
def get_token():
    token = 'qeehfjejwjwjej11sss@22'
    print('#fixture# 获取到token:%s' % token)
    return token

@pytest.fixture()
def login(request):
    """登录"""
    param = request.param
    print(f"用户名：{param['username']}，密码：{param['password']}")
    # 返回
    return {"code": 0, "msg": "登陆成功"}

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
　　每个测试用例执行后，制作测试报告
　　:param item:测试用例对象
　　:param call:测试用例的测试步骤
　　         执行完常规钩子函数返回的report报告有个属性叫report.when
            先执行when=’setup’ 返回setup 的执行结果
            然后执行when=’call’ 返回call 的执行结果
            最后执行when=’teardown’返回teardown 的执行结果
　　:return:
　　"""
    print('------------------------------------')

    # 获取钩子方法的调用结果
    out = yield
    print('用例执行结果', out)

    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    print(out) 
    print(report)
    print(report.when)
    print(f'测试报告：{report}')
    print('步骤 ：%s' % report.when)
    print('nodeid：%s' % report.nodeid)
    print('description:%s' % str(item.function.__doc__))
    print(('运行结果: %s' % report.outcome))