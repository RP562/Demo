
def Demo_function(self):
    import system
    import system.perspective
    system.perspective.print("Hello How are you")
    a = 10
    self.getSibling("Status").prop.text = "Hello"
def hello():
    import system
    import system.perspective
    print("Hello World")
    system.perspective.print("Hello Team")
def newfunc():
    import system
    import system.db
    system.db.runNamedQuery("selectq")
def oldfunc():
    import system
    import system.util
    system.util.getVersion()