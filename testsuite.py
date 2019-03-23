import unittest
from driver import Driver
import xmlrunner




class TestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver('android.config')

    def setUp(self):
        self.driver.log('Starting Test: {}'.format(self._testMethodName))

    def tearDown(self):
        self.driver.log('Test Finished: {}'.format(self._testMethodName))

    @classmethod
    def tearDownClass(cls):
        cls.driver.driver.quit()

    def checkIfFloat(self, value):
        try:
            float(value)
            return True
        except Exception as e:
            self.fail(e)

    def getAccountsLists(self):
        accountView = self.driver.getElement('accountsList')
        accountList = self.driver.getElements('accountElement', baseElement=accountView)

        return accountList


    def test01_InitialAccounts(self):

        accountList = self.getAccountsLists()

        for item in accountList:
            text = self.driver.getElement('accountText', baseElement=item).text
            self.driver.log(text)
            self.assertIn(text, self.driver.ACCOUNTS_LIST_TEXT, 'Checking initial Accounts Names')
        self.assertEqual(len(accountList), len(self.driver.ACCOUNTS_LIST_TEXT), )

    def test02_AccountsInitialBalance(self):

        accountList = self.getAccountsLists()

        for item in accountList:
            text = self.driver.getElement('accountBalance', baseElement=item).text
            self.assertTrue(self.checkIfFloat(text[1:]), 'Checking if it is a float value')
            self.assertEquals(text, self.driver.INITIAL_BALANCE, 'Checking initial Accounts Balance')





if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))