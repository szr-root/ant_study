import datetime
import json

import requests


def feishu_send_massage(message):
    url = "https://open.feishu.cn/open-apis/bot/v2/hook/80095689-1683-411b-b086-56c2715b9867"
    headers = {"Content-Type": "application/json"}
    payload_message = {
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": True,
                "enable_forward": True
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "content": "**【时间】** " + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '\n' + message,
                        "tag": "lark_md"
                    }
                },
                {
                    "tag": "hr"
                },
                {
                    "elements": [
                        {
                            "content": "[详情查看日志](https://ww.baidu.com)",
                            "tag": "lark_md"
                        }
                    ],
                    "tag": "note"
                }
            ],
            "header": {
                "template": "yellow",
                "title": {
                    "content": "【接口自动化运行完成】",
                    "tag": "plain_text"
                }
            }
        }

    }

    requests.request("POST", url, headers=headers, data=json.dumps(payload_message))


if __name__ == '__main__':
    message = "Wooplus Api Test Report\nRun_Total_Number:11\nRun_Passed_Number:10\nRun_Failed_Number: 1\nRun_Error_Number: 0\nRun_Skipped_Number: 0\nRun_Successful_Collagen: 90.9090909090909 %\nRun_Case_Times:19.70s\n"
    feishu_send_massage(message)
