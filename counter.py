import mesop as me

@me.stateclass
class State:
    click: int

def button_click(event: me.ClickEvent):
    state = me.state(State)
    state.click += 1

@me.page(path="/counter")
def main():
    state = me.state(State)
    me.text(f"Clicks: {state.click}")
    me.button("Click me!!", on_click=button_click)

    