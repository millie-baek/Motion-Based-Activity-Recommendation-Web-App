import webbrowser
import modi
import time


# html directory here
def open_html_file():
    html_file = 'C:\project_iot\우리 친해요 프로젝트 사이트.html'
    webbrowser.open(html_file)


# button click and double click also can allocate some order
# just btn click > break > next order open()
# what we use pymodi btn is something like remote control button, turn on

if __name__ == "__main__":
    bundle = modi.MODI()
    button = bundle.buttons[0]

    while True:
        if button.pressed:
            print("pressed       ", end='\r')
            break
        else:
            print("not pressed   ", end='\r')
#        if button.double_clicked:
#            print("double clicked", end='\r')
#            break
        time.sleep(0.02)

        

# Call the function to open the HTML file when the button is pressed
open_html_file()
