import requests

class Test_new_joke():
    """Create a new joke"""

    def __init__(self):
        pass

    # def test_create_new_random_joke(self):
    #     """Creation a random joke"""
    #
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print("Status code: " + str(result.status_code))
    #     assert result.status_code == 200
    #     if result.status_code == 200:
    #         print("Test passed")
    #     else:
    #         print("Test failed")
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #     check = result.json()
    #     check_info = check.get("categories")
    #     print(check_info)
    #     assert check_info == []
    #     print("Categories are right")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("Chuck is exist")
    #     else:
    #         print("Chuck NOT exist")


    def test_create_new_random_category_joke(self):
        """Creation a random joke in the category"""

        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Status code: " + str(result.status_code))
        assert result.status_code == 200
        if result.status_code == 200:
            print("Test passed")
        else:
            print("Test failed")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == [category]
        print("Categories are right")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck is exist")
        # else:
        #     print("Chuck NOT exist")

# random_joke = Test_new_joke()
# random_joke.test_create_new_random_joke()

sport_joke = Test_new_joke()
sport_joke.test_create_new_random_category_joke()