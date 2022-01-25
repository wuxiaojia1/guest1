from django.test import TestCase
from django.contrib.auth.models import User

class IndexPageTest(TestCase):
    """测试index登陆页面"""

    def  test_index_page_renders_index_template(self):
        """测试index视图"""
        response = self.client.get('/index/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')


class  LoginActionTest(TestCase):
    """ 测试登陆动作"""

    def setUp(self):
        User.objects.create_user('admin',"admin@mail.com",'admin123456')

    def test_add_user(self):
        result = User.objects.get(username='admin')
        self.assertEqual(result.username,'admin')
        self.assertEqual(result.email,'admin@mail.com')

    def test_login_action_username_password_null(self):
        """
        用户密码为空
        :return:
        """
        data = {"username":"","password":""}
        response = self.client.post('/login_action/',data=data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error!",response.content)

    def test_login_action_username_passwor_error(self):
        """"
        用户名密码错误
        """
        data = {"username":"abc","password":"123"}
        response = self.client.post('/login_action/',data=data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error!",response.content)

    def test_login_action_success(self):
        """
        登陆成功
        :return:
        """
        test_data = {"usernmae":"admin","passsword":"admin123456"}
        response = self.client.post("/login_action/",data=test_data)
        self.assertEqual(response.status_code,200)



