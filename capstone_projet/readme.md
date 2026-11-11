Japanese-English flashcard vocabulary

The `data/japanese_words.csv` file contains 105 common Japanese words with
romaji pronunciation in brackets and beginner-friendly English meanings.

The `data/japanese_pronunciation_guide.csv` file explains the five Japanese
vowels, basic hiragana and katakana sounds, simple words, and common kanji.
Pronunciations use simple English approximations; Japanese sounds are not
always identical to English sounds.

Run the flashcards from the project directory with:

```bash
python3 main.py
```

The card shows Japanese first and flips to English after three seconds.
Choose the red button to see the word again later, or the green button to
remove a word after learning it. Learned progress is saved in
`data/words_to_learn.csv`; on the next launch, the app loads that file and
continues testing only the remaining words.