from appium.webdriver.common.mobileby import MobileBy as MB


class Locators:



    accountsList = {
        'android': (MB.XPATH, "//android.support.v7.widget.RecyclerView")
    }

    accountElement = {
        'android': (MB.XPATH, ".//android.widget.FrameLayout")
    }

    accountText = {
        'android': (MB.XPATH, ".//android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[@resource-id='org.gnucash.android:id/primary_text']")
    }

    accountBalance = {
        'android': (MB.XPATH, ".//android.widget.RelativeLayout/android.widget.TextView[@resource-id='org.gnucash.android:id/account_balance']")
    }