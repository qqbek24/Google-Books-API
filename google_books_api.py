# ****_working with google books api (print)
# ****_Autor: Jakub Koziorowski

import json
from urllib.request import urlopen


class g_books:
    google_api_key = "input here proper KEY"

    def search(self, value):
        parms = ("?q=" + value+ '&maxResults=40' + "&key=" + self.google_api_key)
        req1 = urlopen("https://www.googleapis.com/books/v1/volumes" + parms)
        reqj = json.load(req1)
        print("https://www.googleapis.com/books/v1/volumes" + parms)
        items_reqj = reqj["items"]
        x = len(items_reqj)
        for i in range(0, x):
            volume_info = items_reqj[i]["volumeInfo"]
            volume_info_cover = "" if "imageLinks" not in volume_info else volume_info["imageLinks"]

            p_title = "" if "title" not in volume_info else volume_info["title"]
            p_subtitle = "" if "subtitle" not in volume_info else " - " + volume_info["subtitle"]
            title_subtitle = p_title + p_subtitle
            p_author = [0] if "authors" not in volume_info else volume_info["authors"]
            prettify_author = p_author if len(p_author) > 1 else p_author[0]
            p_pub_date = "" if "publishedDate" not in volume_info else volume_info["publishedDate"]
            page_count = 0 if "pageCount" not in volume_info else volume_info["pageCount"]
            p_thumbnail = "" if "thumbnail" not in volume_info_cover else volume_info_cover["thumbnail"]
            p_language = "" if "language" not in volume_info else volume_info["language"]

            volume_info_id = "0" if "industryIdentifiers" not in volume_info else volume_info["industryIdentifiers"]
            if len(volume_info_id) > 1:
                for x_id in range(0, len(volume_info_id)):
                    id_cds = volume_info_id[x_id]
                    id_cdt = 0 if "identifier" not in id_cds else id_cds["identifier"]
                    if len(id_cdt) == 13:
                        p_identifier = id_cdt
            else:
                volume_info_isbn = volume_info_id[0]
                req_identifier = "brak" if "identifier" not in volume_info_isbn else volume_info_isbn["identifier"]
                p_identifier = req_identifier if len(req_identifier) > 1 else req_identifier[1]

            print(f"\nTitle: {title_subtitle}")
            print(f"Author: {prettify_author}")
            print(f"Publication Date: {p_pub_date}")
            print(f"ISBN: {p_identifier}")
            print(f"Page Count: {page_count}")
            print(f"Cover: {p_thumbnail}")
            print(f"language: {p_language}")
            print("\n***\n")


if __name__ == "__main__":
    bk = g_books()
    bk.search("Tolkien")
