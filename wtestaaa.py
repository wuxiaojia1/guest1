#coding:utf-8
import unittest
from module import Calculator

#引入测试套件
class  ModuleTest(unittest.TestCase):

    #初始化，用开始执行
    def setUp(self):
        self.cal = Calculator(3,4)

     #用例结束
    def tearDown(self):
        pass

    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result,2)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result,-1)

    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result,12)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result,0.75)


if __name__ == "__main__":
    #unittest.main()
    #构建测试集
    suite = unittest.TestSuite()
    #加入测试用例
    suite.addTest(ModuleTest("test_add"))


    #执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)



