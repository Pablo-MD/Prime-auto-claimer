import time 
import os
from pywinauto import Application
from pywinauto import findwindows


def redeem(key):
    try:
        gog = Application(backend='uia').start(r"C:\Program Files (x86)\GOG Galaxy\GalaxyClient.exe", timeout=20)
        print(findwindows.find_elements())
        main_window = gog.window()
        main_window.print_control_identifiers()
        time.sleep(3)
        add_game_button = main_window.child_window(title="Add games & friends", control_type="Button").wrapper_object()
    except:
        gog = Application(backend='uia').connect(path = r"C:\Program Files (x86)\GOG Galaxy\GalaxyClient.exe")
        main_window = gog.window()
        main_window.print_control_identifiers()
        time.sleep(3)
        add_game_button = main_window.child_window(title="Add games & friends", control_type="Button").wrapper_object()

    add_game_button.click_input()
    # main_window.child_window(title="OK", control_type="Button").wrapper_object().click_input()
    main_window.child_window(title="Redeem GOG code", control_type="Button").wrapper_object().click_input()
    main_window.child_window(title=" account.", control_type="Text").wrapper_object().type_keys(key)
    try:
        main_window.child_window(title="Continue", control_type="Button").wrapper_object().click_input()
        main_window.child_window(title="Redeem", control_type="Button").wrapper_object().click_input()
        main_window.child_window(title="OK", control_type="Button").wrapper_object().click_input()
    except:
        main_window.child_window(title="Cancel", control_type="Button").wrapper_object().click_input()
