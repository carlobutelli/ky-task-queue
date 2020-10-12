#!/usr/bin/env python3
from urllib import request
from bs4 import BeautifulSoup

import time


def count_words(url):

    print(f"Counting words at {url}")

    start = time.time()

    r = request.urlopen(url)

    soup = BeautifulSoup(r.read().decode(), "lxml")

    paragraphs = " ".join([p.text for p in soup.find_all("p")])

    word_count = dict()

    for i in paragraphs.split():
        if i not in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1

    end = time.time()

    time_elapsed = end - start

    print(word_count)
    print(f"Total words: {len(word_count)}")
    print(f"Time elapsed: {time_elapsed} ms")

    return len(word_count)
