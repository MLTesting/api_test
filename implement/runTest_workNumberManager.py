import pytest


if __name__ == '__main__':
    pytest.main(['../testUseCases/workNumberManager/test_workNumberManager.py',
                 '--html=../report/test_workNumberManager.html',
                 '--result-log=../log/test_workNumberManager.log'
                 ])


