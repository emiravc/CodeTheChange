from typing import Dict, List, Tuple, Union

from pyrogram.types import InlineKeyboardButton as InlineKB

from prodil.BotConfig import api


class Local:
    QUESTION = "Whats your preferences of resources"
    ANSWER = {
        "AU": "Only Audio",
        "VID": "Only Video",
        "__": "Both video and audio",
    }


class Content:
    QUESTION = "What type of resource you are looking for?"
    ANSWER = {
        "CS": "Counseling Session",
        "OL": "Online Self Help",
    }


class Category:
    QUESTION = "Who are you?"

    @property
    def ANSWER(self):
        categories = api.get_categories()
        return {i["name"]: i["name"] for i in categories}


class Question:
    Local = Local()
    Content = Content()
    Category = Category()

    LEVEL = "level"
    LOCAL = "local"
    CONTENT = "content"
    CATEGORY = "category"

    def get_question(self, question: str) -> str:
        return getattr(self, question.title()).QUESTION

    def get_answer(self, question: str) -> Dict[str, str]:
        return getattr(self, question.title()).ANSWER

    def get_choices(self, question: str) -> Tuple[str, Dict[str, str]]:
        return self.get_question(question), self.get_answer(question)

    def get_categories(self):
        return self.Category.QUESTION, self.Category.answer()


quest = Question()


def slicer(button_list: List[InlineKB], size: int) -> List[List[InlineKB]]:
    return [button_list[i : i + size] for i in range(0, len(button_list), size)]


def make_buttons(answer: Dict[str, str], size: int, back: Union[str, bool]) -> List[List[InlineKB]]:
    buttons = [InlineKB(text=v, callback_data=k) for k, v in answer.items()]
    buttons = slicer(buttons, size)

    if back:
        back_button: InlineKB = InlineKB(text="Go Back", callback_data=back)
        buttons.append([back_button])

    return buttons


def content_buttons(num: int) -> List[List[InlineKB]]:
    buttons = [InlineKB(text=f"🔴 {i+1}", callback_data=str(i + 1)) for i in range(num)]
    buttons = slicer(buttons, 4)
    return buttons