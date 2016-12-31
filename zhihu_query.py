from zhihu_oauth import ZhihuClient


class Topic:
    def __init__(self, name):
        self.name = name
        self.voteup = 0
        self.answer_count = 0

    def add_voteup(self, number):
        self.voteup += number

    def add_answer_count(self, number):
        self.answer_count += number

    def get_voteup(self):
        return self.voteup

    def get_answer_count(self):
        return self.answer_count


client = ZhihuClient()
login_name = input("Please input login ID:")
password = input("Password:")
client.login(login_name, password)
me = client.me()
count_dict = {}
for answer in me.answers:
    for topic in answer.question.topics:
        if topic.name not in count_dict:
            count_dict[topic.name] = Topic(topic.name)
        count_dict[topic.name].add_voteup(answer.voteup_count)
        count_dict[topic.name].add_answer_count(1)

count_list = []
for key in count_dict:
    count_list.append((key, count_dict[key]))
count_list.sort(key=lambda x: x[1].get_answer_count(), reverse=True)
for topic in count_list:
    print("{} : Vote {} : Answer Number {}".format(topic[0], topic[1].get_voteup(), topic[1].get_answer_count()))


