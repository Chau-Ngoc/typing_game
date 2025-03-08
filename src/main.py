import random

import pygame
import requests
from lxml import etree

from src.paragraph import Paragraph

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

with open("topics.txt", "r") as f:
    topics = f.readlines()

topic = random.choice(topics).strip()
rand_start = random.randrange(5)

params = {"search_query": topic, "max_results": 1, "start": rand_start}
url = "http://export.arxiv.org/api/query"
response = requests.get(url, params=params)


def get_article_summary_from_xml(xml) -> str:
    root = etree.fromstring(xml)
    root_tag = etree.QName(root)
    return root.findtext(".//x:summary", namespaces={"x": root_tag.namespace}).strip()


summary_from_xml = get_article_summary_from_xml(response.content)
summary: Paragraph = Paragraph.clean(summary_from_xml)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode == summary.get_char():
                summary.shift_pointer()

    screen.fill("purple")

    # RENDER YOUR GAME HERE
    current_idx = summary.current_idx
    font = pygame.font.SysFont(["DejaVu Sans", "Lato", "Nimbus Sans", "FreeMono", "FreeSans"], 24)
    entire_paragraph = font.render(str(summary), True, (255, 255, 255), wraplength=WINDOW_WIDTH)
    typed = font.render(str(summary[:current_idx]), True, (0, 255, 0), wraplength=WINDOW_WIDTH)

    screen.blit(entire_paragraph, (10, 10))
    screen.blit(typed, (10, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
