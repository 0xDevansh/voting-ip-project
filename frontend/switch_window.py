def switch_window(current_window, window_to_switch):
    def switcher():
        if window_to_switch.state() == 'withdrawn':
            window_to_switch.deiconify()
            current_window.withdraw()
        else:
            window_to_switch.withdraw()
            current_window.deiconify()
    return switcher