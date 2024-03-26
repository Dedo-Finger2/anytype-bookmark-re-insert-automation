import pyautogui as pyauto
import pyperclip as clip
from time import sleep

pyauto.PAUSE = 1

BOOKMARK_TARGET_EXAMPLE_IMAGE = "./assets/bookmark-target.png"
BOOKMARK_URL_COPY_LINK_BUTTON_IMAGE = "./assets/copy-link.png"
BOOKMARK_DELETE_BUTTON = "./assets/delete-button.png"
WEB_CLIPPER_BUTTON = "./assets/web-clipper.png"
SAVE_BUTTON = "./assets/save-button.png"
ANYTYPE_TASKBAR = "./assets/anytype.png"

# 1. Abrir AnyType em maximizado;
# pyauto.press("win")
# pyauto.write("AnyType")
# pyauto.press("enter")

sleep(5)
# 2. Ir até a database de Bookmarks;
pyauto.hotkey("ctrl", "k")
pyauto.write("Bookmarks")
pyauto.press("down")
pyauto.press("enter")

# 3. Procurar por um bookmark que tenha o nome Untitled;
untitled_bookmarks = pyauto.locateAllOnScreen(BOOKMARK_TARGET_EXAMPLE_IMAGE)

for untitled_bookmark in untitled_bookmarks:
    sleep(2)

    # 4. Clicar no bookmark;
    pyauto.click(untitled_bookmark)

    # 5. Copiar a URL do bookmark;
    pyauto.click(928, 310)
    copy_link_button = pyauto.locateCenterOnScreen(BOOKMARK_URL_COPY_LINK_BUTTON_IMAGE)
    pyauto.click(copy_link_button)

    # 6. Deletar o bookmark;
    pyauto.click(1394, 109)

    untitled_bookmark_delete = pyauto.locateCenterOnScreen(BOOKMARK_DELETE_BUTTON)
    pyauto.click(untitled_bookmark_delete)

    # 7. Abrir o navegador maximizado;
    pyauto.press("win")
    pyauto.write("Edge")
    pyauto.press("enter")

    sleep(2)

    # 8. Colar a URL do bookmark;
    pyauto.hotkey("ctrl", "v")
    pyauto.press("enter")

    sleep(4)

    # 9. Clicar na extensão do Web Clipper;
    web_clipper = pyauto.locateCenterOnScreen(WEB_CLIPPER_BUTTON)
    pyauto.click(web_clipper)

    # 10. Remover indicador de notificações do nome do Web Clipper;

    pyauto.hotkey("ctrl", "a")
    pyauto.hotkey("ctrl", "c")

    bookmark_old_title = clip.paste()

    if bookmark_old_title.endswith("YouTube"):
        bookmark_new_title = bookmark_old_title.split(") ")[1] or bookmark_old_title.split(") ")[0]

        pyauto.write(bookmark_new_title)

    # 11. Clicar em salvar;
    save_button = pyauto.locateCenterOnScreen(SAVE_BUTTON)
    pyauto.click(save_button)

    sleep(3)

    pyauto.hotkey("ctrl", "w")

    # 12. Repetir.
print("Done!")