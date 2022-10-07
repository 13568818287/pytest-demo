import pytest
import allure



 
datas = [
    {"username": "name1", "password": "pwd1"},
    {"username": "name2", "password": "pwd2"},
    {"username": "name3", "password": "pwd3"}
]
 
@allure.story('登录功能')
@pytest.mark.parametrize('login', datas, indirect=True)
def test_login(login):
    """
    登录测试用例,利用conftest中的login夹具
    """
    assert login['code'] == 0

test_data = [{"test_input": "3+5",
              "expected": 8,
              "id": "验证3+5=8"
              },
             {"test_input": "2+4",
              "expected": 6,
              "id": "验证2+4=6"
              },
             {"test_input": "6 * 9",
              "expected": 42,
              "id": "验证6*9=42"
              }
             ]

def pytest_generate_tests(metafunc):
    ids = []
    if "parameters" in metafunc.fixturenames:
        for data in test_data:
            ids.append(data['id'])
        # 用test_data这个列表对parameters进行参数化。
        metafunc.parametrize("parameters",test_data, ids=ids, scope="function")


def test_eval(parameters):
    '''验证pytest局部钩子,仅限于本文件,其他的测试文件并不共享。'''
    assert eval(parameters['test_input']) == parameters['expected']


if __name__ == '__main__':  # 定义主函数
    pytest.main()