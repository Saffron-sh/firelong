#!/usr/bin/env python

import subprocess

def smartlink(link):
    if "://" not in link:
        link = "https://" + link
    return link

mainstream = {
        "wa":"https://web.whatsapp.com",
        "whatsapp":"https://web.whatsapp.com",
        "yt":"https://m.youtube.com",
        "youtube":"https://m.youtube.com",
        "ig":"https://instagram.com",
        "insta":"https://instagram.com",
        "instagram":"https://instagram.com",
        "git":"https://github.com",
        "gh":"https://github.com/saffron-sh/",
        "discord":"https://discord.com",
        "linkedin":"https://linked.in",
        "me":"https://archlinux.org",
        "mine":"https://blackarch.org",
        "mail":"https://app.tuta.com",
        "pmail":"https://mail.proton.me"
        }

def show_all():
    for i in enumerate(mainstream.items()):
        print(i[1])

tabs = input("How many:")
links = []

if tabs == "ns":
    while True:
        new_tab = input(">>").lower()
        
        if new_tab == "done":
            break
        elif new_tab == "list":
            show_all()

        else:
            if new_tab in mainstream:
                links.append(mainstream[new_tab])
            else:
                links.append(smartlink(new_tab))
else:
    for i in range(int(tabs)):
        new_tab = input(">>").lower()
        
        if new_tab == "list":
            show_all()
        elif new_tab in mainstream:
            links.append(mainstream[new_tab])
        else:
            links.append(smartlink(new_tab))

links = ["firefox"]+links

subprocess.run(links)
