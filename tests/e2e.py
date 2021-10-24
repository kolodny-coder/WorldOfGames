from selenium import webdriver


class TestScore:
    def test_scores_service(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get('http://localhost:5000/')
        score = driver.find_element_by_id('score').text
        if 1 < int(score) < 1000:
            return True
        else:
            return False

    def main_function(self):
        result = self.test_scores_service()
        if result is True:
            exit()
        else:
            exit(1)


if __name__ == '__main__':
    test1 = TestScore()
    test1.main_function()
