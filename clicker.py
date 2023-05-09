import pyautogui



def clicker(q : list[[int, int]]):
    while len(q) > 0:
        cur = q.pop(0)
        cur_click = [table_left_corner[0] + cur[0] * width_one_dot, table_left_corner[1] + cur[1] * width_one_dot ]
        pyautogui.click(cur_click[0], cur_click[1])
        pyautogui.sleep(0.1)
