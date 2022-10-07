import pytest
import os
import allure


if __name__ == '__main__':
    
    pytest.main(['-vs','--html=./resport-html/index.html','--self-contained-html'])
    
    # pytest.main(['-vs','--alluredir','./result/'])   # 标签名不需要加引号

    # python代码执行
    # os.system('allure generate ./result -o ./allure-report --clean')