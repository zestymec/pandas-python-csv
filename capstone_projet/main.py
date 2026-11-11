import random
from pathlib import Path
import tkinter as tk

import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Aptos"
CARD_WIDTH = 1200
CARD_HEIGHT = 526
FLIP_DELAY = 3000

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data" / "japanese_words.csv"
WORDS_TO_LEARN_FILE = PROJECT_DIR / "data" / "words_to_learn.csv"
IMAGE_DIR = PROJECT_DIR / "images"


def load_words() -> list[dict[str, str]]:
    source_file = (
        WORDS_TO_LEARN_FILE if WORDS_TO_LEARN_FILE.exists() else DATA_FILE
    )
    words = pd.read_csv(source_file).to_dict(orient="records")
    if not words and source_file == DATA_FILE:
        raise ValueError(f"No vocabulary entries found in {source_file}")
    return words


def save_words(words: list[dict[str, str]]) -> None:
    pd.DataFrame(words, columns=["Japanese", "English"]).to_csv(
        WORDS_TO_LEARN_FILE,
        index=False,
    )


class FlashcardApp:
    def __init__(self, window: tk.Tk, words: list[dict[str, str]]) -> None:
        self.window = window
        self.window.title("Japanese Flashcards")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.words_to_learn = words
        self.current_word: dict[str, str] | None = None
        self.flip_timer: str | None = None

        self.card_front = tk.PhotoImage(file=IMAGE_DIR / "card_front.png")
        self.card_back = tk.PhotoImage(file=IMAGE_DIR / "card_back.png")
        self.right_image = tk.PhotoImage(file=IMAGE_DIR / "right.png")
        self.wrong_image = tk.PhotoImage(file=IMAGE_DIR / "wrong.png")

        self.canvas = tk.Canvas(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            bg=BACKGROUND_COLOR,
            highlightthickness=0,
        )
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.canvas.create_image(
            CARD_WIDTH / 2,
            CARD_HEIGHT / 2,
            image=self.card_front,
            tags="card",
        )

        self.wrong_button = tk.Button(
            image=self.wrong_image,
            highlightthickness=0,
            bd=0,
            bg=BACKGROUND_COLOR,
            activebackground=BACKGROUND_COLOR,
            command=self.show_next_card,
        )
        self.wrong_button.grid(row=1, column=0, pady=20)

        self.right_button = tk.Button(
            image=self.right_image,
            highlightthickness=0,
            bd=0,
            bg=BACKGROUND_COLOR,
            activebackground=BACKGROUND_COLOR,
            command=self.mark_word_known,
        )
        self.right_button.grid(row=1, column=1, pady=20)

        self.show_next_card()

    def show_next_card(self) -> None:
        if self.flip_timer is not None:
            self.window.after_cancel(self.flip_timer)
            self.flip_timer = None

        if not self.words_to_learn:
            self.show_finished_card()
            return

        self.current_word = random.choice(self.words_to_learn)
        self.canvas.itemconfig("card", image=self.card_front)
        self.canvas.delete("title")
        self.canvas.delete("word")
        self.canvas.create_text(
            CARD_WIDTH / 2,
            150,
            text="Japanese",
            font=(FONT_NAME, 40, "italic"),
            fill="black",
            tags="title",
        )
        self.canvas.create_text(
            CARD_WIDTH / 2,
            263,
            text=self.current_word["Japanese"],
            font=(FONT_NAME, 60, "bold"),
            fill="black",
            tags="word",
        )
        self.flip_timer = self.window.after(FLIP_DELAY, self.flip_card)

    def flip_card(self) -> None:
        if self.current_word is None:
            return
        self.canvas.itemconfig("card", image=self.card_back)
        self.canvas.itemconfig("title", text="English", fill="white")
        self.canvas.itemconfig("word", text=self.current_word["English"], fill="white")
        self.flip_timer = None

    def mark_word_known(self) -> None:
        if self.current_word in self.words_to_learn:
            self.words_to_learn.remove(self.current_word)
        save_words(self.words_to_learn)
        self.show_next_card()

    def show_finished_card(self) -> None:
        self.current_word = None
        self.canvas.delete("title")
        self.canvas.delete("word")
        self.canvas.itemconfig("card", image=self.card_front)
        self.canvas.create_text(
            CARD_WIDTH / 2,
            210,
            text="すべて覚えました！",
            font=(FONT_NAME, 38, "bold"),
            tags="title",
        )
        self.canvas.create_text(
            CARD_WIDTH / 2,
            290,
            text="You learned all the words!",
            font=(FONT_NAME, 26),
            tags="word",
        )


def main() -> None:
    window = tk.Tk()
    FlashcardApp(window, load_words())
    window.mainloop()


if __name__ == "__main__":
    main()
