import requests

class Test_new_locations():
    """The work witn new location"""

    def test_create_new_location(self):
        """Creation new location"""

        base_url = "https://rahulshettyacademy.com/"    # base url
        post_resource = "/maps/api/place/add/json"      # resource
        key = "?key=qaclick123"                         # parametry for resources

        """Start method POST"""
        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)
        print("Status code: " + str(result_post.status_code))
        assert result_post.status_code == 200
        if result_post.status_code == 200:
            print("Location created")
        else:
            print("Creation failed")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Status code response: " + check_info_post)
        assert check_info_post == "OK"
        print("Status code is RIGHT")
        place_id = check_post.get("place_id")
        print("ID new location: " + place_id)

        """New location creation checking"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("Status code: " + str(result_get.status_code))
        assert result_get.status_code == 200
        if result_get.status_code == 200:
            print("Location created")
        else:
            print("Creation failed")

        """Update location address"""

        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_address = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json = json_for_update_address)
        print(result_put.text)
        print("Status code: " + str(result_put.status_code))
        assert result_put.status_code == 200
        if result_put.status_code == 200:
            print("Location updated")
        else:
            print("Location NOT updated")
        put_msg = "Address successfully updated"
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print(check_put_info)
        assert check_put_info == put_msg
        print("Response msg is RIGHT")

        """Location change checking"""

        print(get_url)
        result_get_new = requests.get(get_url)
        print(result_get_new.text)
        print("Status code: " + str(result_get_new.status_code))
        assert result_get_new.status_code == 200
        if result_get_new.status_code == 200:
            print("Location checked")
        else:
            print("Location failed")
        check_msg = "100 Lenina street, RU"
        check_new = result_get_new.json()
        check_new_info = check_new.get("address")
        print(check_new_info)
        assert check_new_info == check_msg
        print("New address is RIGHT")


new_place = Test_new_locations()
new_place.test_create_new_location()