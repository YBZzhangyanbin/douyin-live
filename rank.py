import requests
if __name__ == '__main__':
    url = "https://webcast5-normal-lq.amemv.com/webcast/ranklist/hour_detail/?room_id=7369065931135273768&sec_anchor_id=MS4wLjABAAAA6vQ4hh5hJ6DhL_Y2u9QJOjQLmCSVFvOQ74Ocbl_mxw_vplUkGu3QjkE6vXeWI14G&anchor_id=2975757715121639&sec_user_id=0&ranklist_type=23&live_request_from_jsb=1&live_sdk_version=290400&r_signature=ME4EEGua84Brm3g2RTYsNsyVHBwEOL24saRgorgJtwx22OjBB7SI6xqLrpoAA54qDLheJXTxh8Hk0hLhQ8CNWE8sZspRy-NsKOVVdp9gBAABAAAA&webcast_sdk_version=3350&webcast_language=zh&webcast_locale=zh_CN&webcast_gps_access=2&current_network_quality_info=%7B%22http_rtt%22%3A72%2C%22tcp_rtt%22%3A43%2C%22quic_rtt%22%3A43%2C%22downstream_throughput_kbps%22%3A8990%2C%22net_effective_connection_type%22%3A8%2C%22video_download_speed%22%3A5362%2C%22quic_receive_loss_rate%22%3A-1%2C%22quic_send_loss_rate%22%3A-1%7D&device_score=7.5&address_book_access=2&user_id=0&is_pad=false&is_android_pad=0&is_landscape=false&carrier_region=CN&iid=657938608321056&device_id=657938608316960&ac=wifi&channel=douyin-huidu-gw-huidu-2940&aid=1128&app_name=aweme&version_code=290400&version_name=29.4.0&device_platform=android&os=android&ssmix=a&device_type=HD1910&device_brand=OnePlus&language=zh&os_api=28&os_version=9&manifest_version_code=290400&resolution=1080*1920&dpi=480&update_version_code=29400100&_rticket=1715755754015&package=com.ss.android.ugc.aweme&mcc_mnc=46000&first_launch_timestamp=1715753164&last_deeplink_update_version_code=29400100&cpu_support64=true&host_abi=arm64-v8a&is_guest_mode=0&app_type=normal&minor_status=0&appTheme=light&is_preinstall=0&need_personal_recommend=1&is_android_fold=0&ts=1715755753&cdid=c136bbe4-756c-4550-95b8-48d6141125a5"
    payload = {}
    headers = {
      'Cookie': 'passport_csrf_token=5aff74dbdde017c8915fcceb732d50a7; passport_csrf_token_default=5aff74dbdde017c8915fcceb732d50a7; store-region=cn-bj; store-region-src=did; install_id=657938608321056; ttreq=1$1dfba93de874ad25fba179b753bf044425e0d940; odin_tt=9a5f3bf5bbd027872ad05ae9257069c22ac6b39af0fd2e956fb3d9de52132ae39a19cfa0f1c0c31b106ee800ceea1b502e98e6dc7aa5c13f235c799cf2aba4bd50c1798a81a5c0b19095a506163bca52',
      'user-agent': 'com.ss.android.ugc.aweme/290400 (Linux; U; Android 9; zh_CN; HD1910; Build/PQ3A.190605.05081124; Cronet/TTNetVersion:fe32d991 2024-03-18 QuicVersion:92dcb149 2024-03-18)',
      'x-argus': '6lpEZg==',
      'x-gorgon': '8404a0484001eb6858a9199dc550486452c5b926e49bf608b894',
      'x-helios': 'CSjyXkfrliRH0fUAXletSOExEzpI28UxvkQA49INtddrF0Qk',
      'x-medusa': '6VpEZh2yG5w9jZhdPHCMFr2VJX61MwABgBXmI3pcAzCJGEnFYCJN/yhsTDU/agSbXW4Cg3Z4IHuXQgC3szFWp6AIOPhydxnLkYn9T5jr4IIPA2csKIIryWwpI8lPIRpjJ7ls7HdCVIs4RNrOdG+VwaYQNe9e+rDGrRoatCi+sI3HSuzeG5pos6WFuX9ANVIzP6xlnGSl0gYPkPU44Pqwqrc2JfAflInbiIG0dBHLLrJtTuIDJoI4mGkhyNYrJWZx5PEAg+R52Elv1GVLuTRmdOMtLSj7nhajF9t1oHuowXsyCSaz8tlobxHDwORX7OE7WcMXYDi5/GOQb0b7bRUOrL9/zRlkt8/i1tkjCJQIORtURdZrZGQGertpB8tP2EIHgvsYzGpJMRGD/ihRNR3RxY7i4rUQPEZLH9k4DyDR5ziHB3alezYtF30DtE7VrTbIj8LlfIy+NDXlS4JpznvUf6ovnNFsaLJ6H06QX0fZlgfDYGCIvEwfcTlalSTWJcKhbzEDTwi/0kOqQYS3myJpNoHomBYw6ttuG+zJeWXTHsFYttZu8toNXzBU0ogW+8D/OBxrldoGv4P9+DCwNDZsReDG7Bg12iyKsAC+XN1dcBSVErQ2nIWBL1zXrNXUwt82ULtOxl8UJjtMifmU7Fb7HWI0aCbEg6eQDw5WQjxhrlU/Muq2g+JGlWaxkVmhP71NU+ljsN+enujQaqhpIrHkhkDXCipXcVVQ3O3482fxLnvCd5bLel+9PPobCTWB5AmoHTaT1VGjdgJ28AJvT6eDq+f2tzwqGfilFMBnKa8vOGme0w7k6rd5bnH6Dk3KtUE8LQNrD0CJEj9s8WMmddV4JRyTLzHIU18YG9GkEX3mlSldGSTV01HQjGEK6ssXDf45GmdqMOk7owk/Azo3gqI4vnBxc32ZGKZOtaIPQTQnEJoNRGfdPeVvO79oweGfgvmwYWTqBL9F//u/Rf67iDY='
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    rank_list = response.json()
    ranks_100 = []
    ranks_list = rank_list.get("data").get("ranks")
    if len(ranks_list) == 100:
        print("小时人气榜: 成功抓取100人")
        for rank in ranks_list:
            nickname = rank.get("user").get("nickname");
            index = rank.get("index")
            gameName = rank.get("rich_tags_info").get("rich_tags")[1].get("content")
            userId = rank.get("user").get("id")
            ranks_100.append({
                "nickname": rank.get("user").get("nickname"),
                "rank": rank.get("index"),
                "game": rank.get("rich_tags_info").get("rich_tags")[1].get("content"),
                "userId": rank.get("user").get("id"),
            })
            print(f"人气榜: 昵称:{nickname.center(20, ' ')},排名:{index}, 游戏名称:{gameName.center(10, ' ')},用户id:{userId}")
    else:
        print("小时人气榜: 没有抓取到100人,可能数据结构有变动,联系技术吧!!!!")

