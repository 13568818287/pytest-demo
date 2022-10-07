import pytest
class TestOnePytest:
    def setup(self):
        print("#setup#")
    def teardown(self): 
        print("#teardown#")
    @classmethod    
    def setup_class(cls):
        print("# setup_class #")
    @classmethod    
    def teardown_class(cls):
        print("# teardown_class #")
        
    @pytest.mark.demo   
    def test_01(self):
        print("# test_01 case #")
    
    def test2(self,get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test02.py-Test类-test2用例,获取get_token：%s】" %get_token)
        assert get_token == token
