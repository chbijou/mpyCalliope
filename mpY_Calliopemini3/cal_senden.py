import radio 
radio.set_group(1)

def on_forever():
    for index in range(10):
        basic.show_number(index)
        for wdh in range(10):
            radio.send_number(index)
        basic.pause(3000)
basic.forever(on_forever)
