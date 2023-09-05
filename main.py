from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse, parse_qs
from json import load
from http.client import InvalidURL
import os, time, json, random, string, re, ctypes, threading

try:
    import colorama 
    import pystyle
    import datetime
except ModuleNotFoundError:
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install datetime")

from colorama import Fore, Style
from pystyle import Write, System, Colors, Colorate, Anime
from datetime import datetime

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT

output_lock = threading.Lock()
colorama.init()

def get_time_rn():
    date = datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

ctypes.windll.kernel32.SetConsoleTitleW(f'[ Kahoot Answer Hack ] By H4cK3dR4Du#1337 | Support --> https://discord.gg/Un63v2truD')

api = "https://play.kahoot.it/rest/kahoots/"
class Kahoot:
    def __init__(self, uuid):
        self.uuid = uuid
        try:
            if not re.fullmatch(r"^[A-Za-z0-9-]*$", uuid):
                self.data = False
            else:
                self.data = load(urlopen(f"https://play.kahoot.it/rest/kahoots/{uuid}"))
        except HTTPError or InvalidURL:
            self.data = False

    def get_quiz_details(self):
        return {
            "uuid": self.data["uuid"],
            "creator_username": self.data["creator_username"],
            "title": self.data["title"],
            "description": self.data["description"],
            "cover": self.data["cover"]}

    def get_questions(self):
        return self.data["questions"]

    def get_question_names(self):
        questions = []
        for i in range(self.get_quiz_length()):
            if self.get_question_details(i)["type"] == "content":
                questions.append(self.get_question_details(i)["title"])
            else:
                questions.append(self.get_question_details(i)["question"])
        return questions

    def get_quiz_length(self):
        return len(self.data["questions"])

    def get_question_details(self, question):
        if self.data["questions"][question]["type"] == "content":
            data = {
                "type": "content",
                "title": self.data["questions"][question]["title"],
                "description": self.data["questions"][question]["description"]
            }
        else:
            data = {
                "type": self.data["questions"][question]["type"],
                "question": str(self.data["questions"][question]["question"]).replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("<br/>", "\n").replace("</span>", "").replace("</mo>", "").replace("</mrow>", "").replace("<mn>", "").replace("</mn>", "").replace("</annotation>", "").replace("</semantics>", "").replace("</math>", "").replace("<span>", "").replace("<math>", "").replace("<semantics>", "").replace("<mrow>", "").replace("<mo>", "").replace("<msup>", "").replace("<mi>", "").replace("</mi>", "").replace("</msup>", "").replace("<b>", "").replace("</b>", ""),
                "choices": self.data["questions"][question]["choices"],
                "amount_of_answers": len(self.data["questions"][question]["choices"]),
                "amount_of_correct_answers": 0}

            for i in range(len(self.data["questions"][question]["choices"])):
                self.data["questions"][question]["choices"][i]["answer"] = self.data["questions"][question]["choices"][i]["answer"].replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("<br/>", "\n").replace("</span>", "").replace("</mo>", "").replace("</mrow>", "").replace("<mn>", "").replace("</mn>", "").replace("</annotation>", "").replace("</semantics>", "").replace("</math>", "").replace("<span>", "").replace("<math>", "").replace("<semantics>", "").replace("<mrow>", "").replace("<mo>", "").replace("<msup>", "").replace("<mi>", "").replace("</mi>", "").replace("</msup>", "").replace("<b>", "").replace("</b>", "")

            for i in range(len(self.data["questions"][question]["choices"])):
                if self.data["questions"][question]["choices"][i]["correct"]:
                    data["amount_of_correct_answers"] += 1

        if "layout" in self.data["questions"][question]:
            data["layout"] = self.data["questions"][question]["layout"]
        else:
            data["layout"] = None

        if "image" in self.data["questions"][question]:
            data["image"] = self.data["questions"][question]["image"]
        else:
            data["image"] = None

        if "pointsMultiplier" in self.data["questions"][question]:
            data["pointsMultiplier"] = self.data["questions"][question]["pointsMultiplier"]
        else:
            data["pointsMultiplier"] = None

        if "time" in self.data["questions"][question]:
            data["time"] = self.data["questions"][question]["time"]
        else:
            data["time"] = None

        return data

    def get_answer(self, question):
        answers = []
        if self.get_question_details(question)["type"] == "content":
            answers = None

        elif self.get_question_details(question)["type"] == "jumble":
            for i in self.get_question_details(question)["choices"]:
                answers.append(str(i["answer"]).replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("<br/>", "\n").replace("</span>", "").replace("</mo>", "").replace("</mrow>", "").replace("<mn>", "").replace("</mn>", "").replace("</annotation>", "").replace("</semantics>", "").replace("</math>", "").replace("<span>", "").replace("<math>", "").replace("<semantics>", "").replace("<mrow>", "").replace("<mo>", "").replace("<msup>", "").replace("<mi>", "").replace("</mi>", "").replace("</msup>", "").replace("<b>", "").replace("</b>", ""))

        else:
            for i in self.get_question_details(question)["choices"]:
                if i["correct"]:
                    answers.append(str(i["answer"]).replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("<br/>", "\n").replace("</span>", "").replace("</mo>", "").replace("</mrow>", "").replace("<mn>", "").replace("</mn>", "").replace("</annotation>", "").replace("</semantics>", "").replace("</math>", "").replace("<span>", "").replace("<math>", "").replace("<semantics>", "").replace("<mrow>", "").replace("<mo>", "").replace("<msup>", "").replace("<mi>", "").replace("</mi>", "").replace("</msup>", "").replace("<b>", "").replace("</b>", ""))
            if len(answers) == 0:
                answers = None
        return answers
    
def start_kahoot():
    System.Clear()
    Write.Print(f"root@kahoot_link ~> ", Colors.purple_to_blue, interval=0.000); link = input(pretty)
    try:
        parsed_url = urlparse(link)
        query_params = parse_qs(parsed_url.query)
        quiz_id = query_params.get("quizId", [])[0]
        kahoot = Kahoot(quiz_id)
        time_rn = get_time_rn()
        print()
        print(f"{pretty}{time_rn} {reset}| ({magenta}${reset}) Fetching Answers... {pink}[ {reset}{quiz_id} {pink}]\n")
        time.sleep(1)
        for i in range(kahoot.get_quiz_length()):
            if kahoot.get_answer(i) is not None:
                if kahoot.get_question_details(i)['type'] == 'open_ended':
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{pretty}{time_rn} {reset}| ({yellow}*{reset}) Question ---> {pink}[ {reset}{kahoot.get_question_names()[i]} {pink}]{reset}\n{pretty}{time_rn} {reset}| ({green}+{reset}) Answer ----> {pink} [ {reset}{', '.join(kahoot.get_answer(i))}{pink} ]")
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{pretty}{time_rn} {reset}| ({yellow}*{reset}) Question ---> {pink}[ {reset}{kahoot.get_question_names()[i]} {pink}]{reset}\n{pretty}{time_rn} {reset}| ({green}+{reset}) Answer ----> {pink} [ {reset}{', '.join(kahoot.get_answer(i))}{pink} ]")
            time.sleep(0.020)
    except:         
        start_kahoot()

Write.Print(f"""

""", Colors.purple_to_blue, interval=0.000)
start_kahoot()
Write.Print(f"\nroot@press_enter ~> ", Colors.purple_to_blue, interval=0.000); input(pretty)